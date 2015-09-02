from bs4 import BeautifulSoup
import requests
import pandas as pd
from statistics import median

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
# of values for each attribute. Anything in particular stand out at 
# you? What's the median age and the mean age for each gender? Which 
# do you think is more appropriate for this dataset?

# Mean age men
sum(table['men'].astype(int))/len(table['men'].astype(int))
# Out[117]: 12.24468085106383



