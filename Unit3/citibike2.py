# Requests is a package that allows us to download data from any online resource.
import requests
# Because it's in JSON format, you have to do something a little different to import it:
from pandas.io.json import json_normalize
import matplotlib.pyplot as plt
import pandas as pd
# To use counter:
import collections
from statistics import median
import sqlite3 as lite
# a package with datetime objects
import time
# a package for parsing a string into a Python datetime object
from dateutil.parser import parse 

r = requests.get('http://www.citibikenyc.com/stations/json')

con = lite.connect('citi_bike.db')
cur = con.cursor()

with con:
	cur.execute("DROP TABLE IF EXISTS citibike_reference")
	cur.execute("DROP TABLE IF EXISTS available_bikes")


key_list = [] #unique list of keys for each station listing
for station in r.json()['stationBeanList']:
    for k in station.keys():
        if k not in key_list:
            key_list.append(k)

df = json_normalize(r.json()['stationBeanList'])

with con:
    cur.execute('''CREATE TABLE citibike_reference (
    	id INT PRIMARY KEY, 
    	totalDocks INT, 
    	city TEXT, 
    	altitude INT, 
    	stAddress2 TEXT, 
    	longitude NUMERIC, 
    	postalCode TEXT, 
    	testStation TEXT, 
    	stAddress1 TEXT, 
    	stationName TEXT, 
    	landMark TEXT, 
    	latitude NUMERIC, 
    	location TEXT )''')

    # Populate with values
    #a prepared SQL statement we're going to execute over and over again
sql = '''INSERT INTO citibike_reference (
	id, 
	totalDocks, 
	city, 
	altitude, 
	stAddress2, 
	longitude, 
	postalCode, 
	testStation, 
	stAddress1, 
	stationName, 
	landMark, 
	latitude, 
	location) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)'''

#for loop to populate values in the database
with con:
    for station in r.json()['stationBeanList']:
        #id, totalDocks, city, altitude, stAddress2, longitude, postalCode, testStation, stAddress1, stationName, landMark, latitude, location)
        cur.execute(sql,(station['id'],station['totalDocks'],station['city'],station['altitude'],station['stAddress2'],station['longitude'],station['postalCode'],station['testStation'],station['stAddress1'],station['stationName'],station['landMark'],station['latitude'],station['location']))


# To get multiple readings by minute, the availablebikes table is going 
# to need to be a little different. In this case, the station ID (id) 
# is going to be the column name, but since the column name can't 
# start with a number, you'll need to put a character in front of the 
# number ("").

# With 332 stations, this is best done in code:
#extract the column from the DataFrame and put them into a list
station_ids = df['id'].tolist() 

#add the '_' to the station name and also add the data type for SQLite
station_ids = ['_' + str(x) + ' INT' for x in station_ids] 

#create the table
#in this case, we're concatentating the string and joining all the station ids (now with '_' and 'INT' added)

with con:
	cur.execute("CREATE TABLE available_bikes ( execution_time INT, " +  ", ".join(station_ids) + ");")



for i in range(60):
    
    # r = requests.get('http://www.citibikenyc.com/stations/json')
    exec_time = parse(r.json()['executionTime'])

    cur.execute('INSERT INTO available_bikes (execution_time) VALUES (?)', (exec_time.strftime('%s'),))
    con.commit()

    id_bikes = collections.defaultdict(int)
    for station in r.json()['stationBeanList']:
        id_bikes[station['id']] = station['availableBikes']

    for k, v in id_bikes.items():
        cur.execute("UPDATE available_bikes SET _" + str(k) + " = " + str(v) + " WHERE execution_time = " + exec_time.strftime('%s') + ";")
    con.commit()

    time.sleep(60)

con.close() #close the database connection when done


# ANALYZING THE RESULTS

# Reading in the data:
df = pd.read_sql_query("SELECT * FROM available_bikes ORDER BY execution_time",con,index_col='execution_time')

# First you need to process each column and calculate the change each minute:
hour_change = collections.defaultdict(int)
for col in df.columns:
    station_vals = df[col].tolist()
    station_id = col[1:] #trim the "_"
    station_change = 0
    for k,v in enumerate(station_vals):
        if k < len(station_vals) - 1:
            station_change += abs(station_vals[k] - station_vals[k+1])
    hour_change[int(station_id)] = station_change #convert the station id back to integer

# The enumerate() function returns not only the item in the list but 
# also the index of the item. This allows us to find the value 
# (with index of k) just after it in sequence (k + 1). We run the loop 
# until k is equal to the index for the second to last element in the list.

# At this point, the values are in the dictionary keyed on the station ID. 
# To find the winner:

def keywithmaxval(d):
    # create a list of the dict's keys and values; 
    v = list(d.values())
    k = list(d.keys())

    # return the key with the max value
    return k[v.index(max(v))]

# assign the max key to max_station
max_station = keywithmaxval(hour_change)

# From there, you query the reference table for the important 
# information about the most active station:

#query sqlite for reference information
cur.execute("SELECT id, stationname, latitude, longitude FROM citibike_reference WHERE id = ?", (max_station,))
data = cur.fetchone()
print "The most active station is station id %s at %s latitude: %s longitude: %s " % data
print "With " + str(hour_change[379]) + " bicycles coming and going in the hour between " + datetime.datetime.fromtimestamp(int(df.index[0])).strftime('%Y-%m-%dT%H:%M:%S') + " and " + datetime.datetime.fromtimestamp(int(df.index[-1])).strftime('%Y-%m-%dT%H:%M:%S')

# This should print out the result. 
# Note that this will just print out the first station in the list that 
# has the max value. You should visually inspect the data to make sure 
# this is the case:

plt.bar(hour_change.keys(), hour_change.values())
plt.show()





