# Challenge: Write a script called "database.py" to print out the cities with the 
# July being the warmest month. Your script must:

# Connect to the database
import sqlite3 as lite
import pandas as pd

con = lite.connect('getting_started.db')

# Define table variables
cities = (('New York City', 'NY'),
    ('Boston', 'MA'),
    ('Chicago', 'IL'),
    ('Miami', 'FL'),
    ('Dallas', 'TX'),
    ('Seattle', 'WA'),
    ('Portland', 'OR'),
    ('San Francisco', 'CA'),
    ('Los Angeles', 'CA'))

weather = (('New York City', 2013, 'July', 'January', 62),
    ('Boston', 2013, 'July', 'January', 59),
    ('Chicago', 2013, 'July', 'January', 59),
    ('Miami', 2013, 'August', 'January', 84),
    ('Dallas', 2013, 'July', 'January', 77),
    ('Seattle', 2013, 'July', 'January', 61),
    ('Portland', 2013, 'July', 'December', 63),
    ('San Francisco', 2013, 'September', 'December', 64),
    ('Los Angeles', 2013, 'September', 'December', 75))

# Create the cities and weather tables (HINT: first pass the statement DROP TABLE 
# IF EXISTS <table_name>; to remove the table before you execute the CREATE TABLE ... statement)

with con:
	cur = con.cursor()
	cur.execute("DROP TABLE IF EXISTS cities")
	cur.execute("DROP TABLE IF EXISTS weather")
	cur.execute("CREATE TABLE cities (name text, state text)")
	cur.execute("CREATE TABLE weather(city text, year integer, warm_month text, cold_month text, average_high integer)")

# Insert data into the two tables
# DEFINED TABLE VALUES AT TOP
	cur.executemany("INSERT INTO cities VALUES(?,?)", cities)
	cur.executemany("INSERT INTO weather VALUES(?,?,?,?,?)", weather)

# Join the data together
	cur.execute('''SELECT name, state, year, warm_month, cold_month, average_high
				FROM cities 
				INNER JOIN weather 
    			ON name = city
				WHERE warm_month="July"
				ORDER BY average_high DESC''');

# Load into a pandas DataFrame

	rows = cur.fetchall()
	cols = [desc[0] for desc in cur.description]
	df = pd.DataFrame(rows, columns=cols)

# Print out the resulting city and state in a full sentence. For example: 
# "The cities that are warmest in July are: Las Vegas, NV, Atlanta, GA..."
	
	print("The cities that are the warmest in July are:")
	for i in range(len(df)): 
		print(df['name'].ix[i].strip(' ')+", "+df['state'].ix[i])

		# trim

# Push your code to Github and enter the link below


# Challenge
# Try to write this script so the input can be more dynamic. Either take in the 
# name of a month or have the user enter the value interactively. Query the 
# database and return a result. Remember you'll have to handle all kinds of input. 
# You take in command line input using the sys package. Don't spend too much time 
# on this, especially if you've never programmed before. Dynamic input is one way 
# to make code more functional but won't be a necessity going forward. You can find