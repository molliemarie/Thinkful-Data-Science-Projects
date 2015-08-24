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


r = requests.get('http://www.citibikenyc.com/stations/json')
# At this point, the file is in Python and we can manipulate it from there.
# Documentation for Requests package: http://docs.python-requests.org/en/latest/

# # Basic view of text:
# r.text

# # View Json notation
# r.json()

# # View keys
# r.json().keys()
# # Out[10]: dict_keys(['stationBeanList', 'executionTime'])

# # Find time item the file was created:
# r.json()['executionTime']
# # '2015-08-21 03:27:13 AM'

# # See a list of stations
# r.json()['stationBeanList']

# # To get number of docks
# print('number of docks is: ', len(r.json()['stationBeanList']))
# # Out[13]: 509

# You can test that you have all the fields (important for setting up a database) 
# by running the data through a loop and gathering all the fields together:

key_list = [] #unique list of keys for each station listing
for station in r.json()['stationBeanList']:
    for k in station.keys():
        if k not in key_list:
            key_list.append(k)

# key_list
# # Out[17]: 
# # ['availableDocks',
# #  'id',
# #  'altitude',
# #  'totalDocks',
# #  'longitude',
# #  'lastCommunicationTime',
# #  'city',
# #  'statusValue',
# #  'stationName',
# #  'location',
# #  'landMark',
# #  'postalCode',
# #  'availableBikes',
# #  'latitude',
# #  'testStation',
# #  'stAddress2',
# #  'statusKey',
# #  'stAddress1']

# # To get the first list:
# r.json()['stationBeanList'][0]
# # Out[18]: 
# # {'altitude': '',
# #  'availableBikes': 27,
# #  'availableDocks': 10,
# #  'city': '',
# #  'id': 72,
# #  'landMark': '',
# #  'lastCommunicationTime': '2015-08-21 03:25:31 AM',
# #  'latitude': 40.76727216,
# #  'location': '',
# #  'longitude': -73.99392888,
# #  'postalCode': '',
# #  'stAddress1': 'W 52 St & 11 Ave',
# #  'stAddress2': '',
# #  'stationName': 'W 52 St & 11 Ave',
# #  'statusKey': 1,
# #  'statusValue': 'In Service',
# #  'testStation': False,
# #  'totalDocks': 39}

df = json_normalize(r.json()['stationBeanList'])
# Notice we're taking the stationBeanList and passing values associated 
# with it to pandas to create a DataFrame out of the data instead of the 
# whole JSON. We end up with a standard DataFrame like we've used in the past lessons.

# Range of values starting with available bikes
df['availableBikes'].hist()
plt.show()

# Range of total docks:
plt.close()
df['totalDocks'].hist()
plt.show()

# Explore the other data variables. 
# Are there any test stations? 
t = collections.Counter(df['testStation'])
print('Number of Test Stations: ', t['True'])
# Number of Test Stations:  0
# No, there are no test stations

# How many stations are "In Service"? 
# Count number of instances per situation
c = collections.Counter(df['statusValue'])
# calculate the number of instances in the list
print('Stations in Service:', c['In Service'])
# Stations in Service: 386

# How many are "Not In Service"? 
print('Stations Not in Service:', c['Not In Service'])
# Stations Not in Service: 124

# Any other interesting variables values that need to be accounted for?


# What is the mean number of bikes in a dock? 
# Count number of instances per number
bikes = collections.Counter(df['availableBikes'])
# calculate the number of instances in the list
bikes_sum = sum(bikes.values())
station_count = len(bikes)
avg_docked = bikes_sum / station_count
print('Average Docked Bikes:', avg_docked)
# Average Docked Bikes per Station: 12.75

# What is the median? 
median_docked = median(df['availableBikes'])
print('Median Docked bikes: ', median_docked)
# Median Docked bikes:  9.5

# How does average change if we remove the stations that aren't in service?
condition = (df['statusValue'] == 'In Service')
print('Average Docked Bikes (Active Stations only): ', df[condition]['totalDocks'].mean())
# Average Docked Bikes per Active Station:  33.6839378238342

# How does median change if we remove stations not in service
print('Median Docked Bikes (Active Stations only): ',df[df['statusValue'] == 'In Service']['totalDocks'].median())
# Median Docked Bikes per Active Station:  31.0

# Create SQL Database:
con = lite.connect('citi_bike.db')
cur = con.cursor()

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
station_ids = ['_' + str(x) + ' INT' for x in station_ids) 

#create the table
#in this case, we're concatentating the string and joining all the station ids (now with '_' and 'INT' added)
with con:
    cur.execute("CREATE TABLE available_bikes ( execution_time INT, " +  ", ".join(station_id) + ");")











