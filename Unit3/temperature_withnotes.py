import sqlite3 as lite
import requests
import datetime

cities = { "Minneapolis": '44.963324,-3.268320',
            "San_Francisco": '37.727239,-123.032229',
            "Sioux_Falls": '43.550116, -96.729280',
            "Tipton": '42.015974, -84.064363',
            "Pheonix": '33.572154,-112.090132'
            # "Abu Dhabi": '24.483103, 54.353026',
            # "Fehmarn": '54.465705, 11.136710'
        }


# CHALLENGE

# Build the API call by combining the string elements in Python 
# for your first city. You can use the datetime.datetime.now() 
# function from the datetime package for the current datetime. You 
# can use the datetime.timedelta() function to subtract or add time 
# to a date. In this case, we'll be subtracting 30 days from the 
# current date to get our start date and then iterating through 
# until the present day. We do that like this 
# start_date = datetime.datetime.now() - datetime.timedelta(days=30). 
# This will subtract 30 days from the current day.

end_date = datetime.datetime.now() # by setting this equal to a variable, we fix the calculation to the point when we started the scrip (rather than have things move aroudn while we're coding.)
query_date = end_date - datetime.timedelta(days=30) #the current value being processed

# Test the call for your first city and make sure you have it formatted 
# properly. You can start by just printing out the URL and pasting it 
# into your browser before you use the requests package to do the call 
# for you. This can help you troubleshoot any errors (though you can use 
# the text and status_code attributes to also troubleshoot any errors)

API_KEY = '66a4ee1dd841976fcf36a94a3b3b930e'
URL =  "https://api.forecast.io/forecast/" + API_KEY + "/" # LATITUDE,LONGITUDE,TIME
# URL: https://api.forecast.io/forecast/66a4ee1dd841976fcf36a94a3b3b930e/

# Once you have the URL formatted properly, issue the request from 
# your code and inspect the result. How many levels does the data have? 
# Which field do we want to save to get the daily maximum temperature?

con = lite.connect('weather.db')
cur = con.cursor()

cities.keys()
# Out[23]: dict_keys(['Abu Dhabi', 'Tipton', 'San Francisco', 'Pheonix', 'Minneapolis', 'Fehmarn', 'Sioux Falls'])

# Based on the data sample, create the table in a SQLite database 
# called "weather.db".

	# Create table
with con:
    cur.execute("DROP TABLE IF EXISTS daily_temp")
    cur.execute('CREATE TABLE daily_temp ( day_of_reading INT, Minneapolis REAL, San_Francisco REAL, Sioux_Falls REAL, Tipton REAL, Pheonix REAL);') #use your own city names instead of city1...
	# In SQL, a row has to be inserted before it can be updated. In order 
	# to keep the code clean, we're going to iterate through the values in 
	# the range and insert them into the database without any other values
with con:
    while query_date < end_date:
        cur.execute("INSERT INTO daily_temp(day_of_reading) VALUES (?)", (int(query_date.strftime('%s')),))
        query_date += datetime.timedelta(days=1)


    # Now we can loop through our cities and query the API:

for k,v in cities.items():
    query_date = end_date - datetime.timedelta(days=30) #set value each time through the loop of cities
    while query_date < end_date:
        #q


# Write a script that takes each city and queries every day for the past 
# 30 days (Hint: You can use the datetime.timedelta(days=1) to increment 
# 	the value by day)

# Save the max temperature values to the table, keyed on the date. You can 
# uery for the value
    r = requests.get(URL + v + ',' +  query_date.strftime('%Y-%m-%dT12:00:00'))

    with con:
            #insert the temperature max to the database
        cur.execute('UPDATE daily_temp SET ' + k + ' = ' + str(r.json()['daily']['data'][0]['temperatureMax']) + ' WHERE day_of_reading = ' + query_date.strftime('%s'))

        #increment query_date to the next day for next operation of loop
    query_date += datetime.timedelta(days=1) #increment query_date to the next day


con.close() # a good practice to close connection to database# leave the date in Unix time or convert to a string.




