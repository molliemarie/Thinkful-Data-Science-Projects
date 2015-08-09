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
    			ON name = city''')

# Load into a pandas DataFrame

	rows = cur.fetchall()
  	cols = [desc[0] for desc in cur.description]
  	df = pd.DataFrame(rows, columns=cols)

# Print out the resulting city and state in a full sentence. For example: 
# "The cities that are warmest in July are: Las Vegas, NV, Atlanta, GA..."

#NOT SURE HOW TO DO THIS - I know how to write the SQL code to return the cities
# that are hottest in July, but not sure how to then put them into the print code

	cur.execute('''SELECT name, state, warm_month
	FROM cities 
	INNER JOIN weather 
    	ON name = city
	WHERE warm_month="July"''');

	# print("The cities that are the warmest in July are: [insert cities here somehow...]")
    #  Maybe something like below?

    city = df[0]
    state = df[1]
    warm_month = df[4]

    for row in rows:
    	if warm_month = "July":
    		print("The cities that are hottest in July are: {0}, {1}".format(city, state))

    



    # ANOTHER USER'S SOLUTION - seems like it could be simpler than this...

    #index into df to get city, state pairs 
    # warmest = zip(df["name"], df["state"])
    
    # if len(warmest) == 1:
    #     print("The city that is warmest in {} is: ".format(user_month) +
    #           "{}, {}".format(warmest[0][0], warmest[0][1]))
    # elif len(warmest) > 1:
    #     warmest_string = ""
    #     for pair in warmest[:-1]:
    #         warmest_string += "{}, {}, ".format(pair[0], pair[1])
    #     warmest_string += "and {}, {}.".format(warmest[-1][0], warmest[-1][1])

    #     print("The cities that are warmest in {} are: ".format(user_month) +
    #           warmest_string)
    # else:
    #     print("No cities have {} as their warmest month.".format(user_month))




# Push your code to Github and enter the link below

# Submit your code using the link below. If you have trouble, be sure to 
# review the material in this lesson, search online resources, and reach out to 
# your mentor. Good luck!

# Challenge
# Try to write this script so the input can be more dynamic. Either take in the 
# name of a month or have the user enter the value interactively. Query the 
# database and return a result. Remember you'll have to handle all kinds of input. 
# You take in command line input using the sys package. Don't spend too much time 
# on this, especially if you've never programmed before. Dynamic input is one way 
# to make code more functional but won't be a necessity going forward. You can find

# STRAIGHT UP SQL CODE, NOT YET CONVERTED TO PYTHON

# Create the cities and weather tables (HINT: first pass the statement DROP TABLE 
# IF EXISTS <table_name>; to remove the table before you execute the CREATE TABLE ... statement)

# DROP TABLE IF EXISTS cities
# DROP TABLE IF EXISTS weather
# CREATE TABLE cities (name text, state text);
# CREATE TABLE weather(city text, year integer, warm_month text, cold_month text, average_high integer)


# Insert data into the two tables

# INSERT INTO cities (name, state) VALUES
#     ('New York City', 'NY'),
#     ('Boston', 'MA'),
#     ('Chicago', 'IL'),
#     ('Miami', 'FL'),
#     ('Dallas', 'TX'),
#     ('Seattle', 'WA'),
#     ('Portland', 'OR'),
#     ('San Francisco', 'CA'),
#     ('Los Angeles', 'CA');

# INSERT INTO weather (city, year, warm_month, cold_month, average_high) VALUES
#     ('New York City', 2013, 'July', 'January', 62),
#     ('Boston', 2013, 'July', 'January', 59),
#     ('Chicago', 2013, 'July', 'January', 59),
#     ('Miami', 2013, 'August', 'January', 84),
#     ('Dallas', 2013, 'July', 'January', 77),
#     ('Seattle', 2013, 'July', 'January', 61),
#     ('Portland', 2013, 'July', 'December', 63),
#     ('San Francisco', 2013, 'September', 'December', 64),
#     ('Los Angeles', 2013, 'September', 'December', 75); 
# plenty of tutorials on how to accept user input online.