# Requests is a package that allows us to download data from any online resource.
import requests
# Because it's in JSON format, you have to do something a little different to import it:
from pandas.io.json import json_normalize
import matplotlib.pyplot as plt
import pandas as pd

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
df['totalDocks'].hist()
plt.show()

# Explore the other data variables. 
# Are there any test stations? 

# How many stations are "In Service"? 

# How many are "Not In Service"? 

# Any other interesting variables values that need to be accounted for?


# What is the mean number of bikes in a dock? 

# What is the median? 

# How does this change if we remove the stations that aren't in service?




