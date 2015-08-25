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

con = lite.connect('citi_bike.db')
cur = con.cursor()

for i in range(60):
	r = requests.get('http://www.citibikenyc.com/stations/json')
	df = json_normalize(r.json()['stationBeanList'])

	with con:
		cur.execute("DROP TABLE IF EXISTS citibike_reference")
		cur.execute("DROP TABLE IF EXISTS available_bikes")

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
	    cur.execute("CREATE TABLE available_bikes ( execution_time INT, " +  ", ".join(station_ids) + ");")

	# Now let's populate it with our values for available bikes:
	#take the string and parse it into a Python datetime object
		exec_time = parse(r.json()['executionTime'])

	# We create an entry for the execution time by inserting it into the database:
	    cur.execute('INSERT INTO available_bikes (execution_time) VALUES (?)', (exec_time.strftime('%s'),))

	# Then we iterate through the stations in the "stationBeanList":
		id_bikes = collections.defaultdict(int) #defaultdict to store available bikes by station

	#loop through the stations in the station list
		for station in r.json()['stationBeanList']:
		    id_bikes[station['id']] = station['availableBikes']

	#iterate through the defaultdict to update the values in the database
	    for k, v in id_bikes.items():
	        cur.execute("UPDATE available_bikes SET _" + str(k) + " = " + str(v) + " WHERE execution_time = " + exec_time.strftime('%s') + ";")

	    con.commit()

	    time.sleep(60)
	con.close()
	# The function strftime() formats the time. It's alternate is strptime(), 
	# which is used to parse a string into the proper time format. For more on 
	# datetime objects in Python, check out the documentation.
















