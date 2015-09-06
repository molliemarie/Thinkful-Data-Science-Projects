from bs4 import BeautifulSoup
import requests
import pandas as pd
from statistics import median
import matplotlib.pyplot as plt
import csv

# Import pages
url = "http://web.archive.org/web/20110514112442/http://unstats.un.org/unsd/demographic/products/socind/education.htm"
r = requests.get(url)

# Pass results to beautiful soup
soup = BeautifulSoup(r.content)

# As the name implies, the webpage content exists 
# as a mess of text in the soup object. We need to 
# extract the table we want, so we start trying to 
# filter through, checking each table for the content we want:

for row in soup('table'):
    print(row)

# The directions say "finally, we see table 7
# has the data we want". How do we know that?
soup('table')[6]

# Now we want to return all the tags. Look through the documentation and see 
# if you can get the elements from the table. You'll still need to process 
# the rows once you retrieve them and deal with the spaces and empty field 
# separators. Do your best and reach out to your mentor if you need help.

A = soup('table')[6].findAll('tr', {'class': 'tcont'})
B = [x for x in A if len(x)== 25] # removing records without value

# Create a table with the country name, the male school life expectancy, 
# the female school life expectancy and the year of the analysis. Create it 
# in Python as we've done in previous examples and insert the data you've scraped. 
# If you have any troubles, ask your mentor for assistance, but hopefully these 
# tasks are becoming more and more familiar to you.

records = []
for rows in B:
    col = rows.findAll('td')
    country = col[0].string
    year = col[1].string
    total = col[4].string
    men = col[7].string
    women = col[10].string
    record = (country, year, total, men, women)
    records.append(record)
    column_name = ['country', 'year', 'total', 'men', 'women']
    table = pd.DataFrame(records, columns = column_name )

# As we have with the previous assignments, look at the distribution 
# of values for each attribute. 

# Histogram of male ages
plt.figure()
(table['men'].astype(int)).hist()
plt.title('Male School Life Expentancy Histogram')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

# Histogram of female ages
plt.close()
plt.figure()
(table['women'].astype(int)).hist()
plt.title('Women School Life Expentancy Histogram')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

# Anything in particular stand out at you? 
# The male ages are distributed more normally, while with females
# There are two distinct peaks at ages 12-15.

# What's the median age and the mean age for each gender? 

# Mean age men
(table['men'].astype(int)).mean()
# Out[162]: 12.24468085106383

# Median age men
median(table['men'].astype(int))
# Out[121]: 12.0

# Mean age women
(table['women'].astype(int)).mean()
# Out[161]: 12.372340425531915

# Median age women
median(table['women'].astype(int))
# Out[125]: 13.0

# # Which do you think is more appropriate for this dataset?
# I think the median is more appropriate for this dataset 



# You're going to compare the school life expectancy statistics 
# you scraped in the previous assignment to national gross domestic 
# product data from the World Bank.

# With a file like this, it's best to read in the file line by line 
# using the technique you were introduced to in the very beginning of 
# the course:

con = lite.connect('education.db')
cur = con.cursor()

with con:
    cur.execute("DROP TABLE IF EXISTS daily_temp")
    # cur.execute('CREATE TABLE ddp ( day_of_reading INT, Minneapolis REAL, San_Francisco REAL, Sioux_Falls REAL, Tipton REAL, Pheonix REAL);') #use your own city names instead of city1...
	

with open('ny.gdp.mktp.cd_Indicator_en_csv_v2/ny.gdp.mktp.cd_Indicator_en_csv_v2.csv','rU') as inputFile:
    next(inputFile) # skip the first two lines
    next(inputFile)
    header = next(inputFile)
    inputReader = csv.reader(inputFile)
    for line in inputReader:
        with con:
            cur.execute('INSERT INTO gdp (country_name, _1999, _2000, _2001, _2002, _2003, _2004, _2005, _2006, _2007, _2008, _2009, _2010) VALUES ("' + line[0] + '","' + '","'.join(line[42:-5]) + '");')






