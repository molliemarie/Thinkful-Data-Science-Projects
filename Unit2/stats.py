import pandas as pd
from scipy import stats

data = '''Region, Alcohol, Tobacco
North, 6.47, 4.03
Yorkshire, 6.13, 3.76
Northeast, 6.19, 3.77
East Midlands, 4.89, 3.34
West Midlands, 5.63, 3.47
East Anglia, 4.52, 2.92
Southeast, 5.89, 3.20
Southwest, 4.79, 2.71
Wales, 5.27, 3.53
Scotland, 6.08, 4.51
Northern Ireland, 4.02, 4.56'''


# data
# Out[19]: 'Region, Alcohol, Tobacco\nNorth, 6.47, 4.03\nYorkshire, 6.13, 3.76\nNortheast, 6.19, 3.77\nEast Midlands, 4.89, 3.34\nWest Midlands, 5.63, 3.47\nEast Anglia, 4.52, 2.92\nSoutheast, 5.89, 3.20\nSouthwest, 4.79, 2.71\nWales, 5.27, 3.53\nScotland, 6.08, 4.51\nNorthern Ireland, 4.02, 4.56'

data = data.splitlines()

# data
# Out[21]: 
# ['Region, Alcohol, Tobacco',
#  'North, 6.47, 4.03',
#  'Yorkshire, 6.13, 3.76',
#  'Northeast, 6.19, 3.77',
#  'East Midlands, 4.89, 3.34',
#  'West Midlands, 5.63, 3.47',
#  'East Anglia, 4.52, 2.92',
#  'Southeast, 5.89, 3.20',
#  'Southwest, 4.79, 2.71',
#  'Wales, 5.27, 3.53',
#  'Scotland, 6.08, 4.51',
#  'Northern Ireland, 4.02, 4.56']

data = [i.split(', ') for i in data]

# data
# Out[23]: 
# [['Region', 'Alcohol', 'Tobacco'],
#  ['North', '6.47', '4.03'],
#  ['Yorkshire', '6.13', '3.76'],
#  ['Northeast', '6.19', '3.77'],
#  ['East Midlands', '4.89', '3.34'],
#  ['West Midlands', '5.63', '3.47'],
#  ['East Anglia', '4.52', '2.92'],
#  ['Southeast', '5.89', '3.20'],
#  ['Southwest', '4.79', '2.71'],
#  ['Wales', '5.27', '3.53'],
#  ['Scotland', '6.08', '4.51'],
#  ['Northern Ireland', '4.02', '4.56']]

column_names = data[0] # this is the first row
data_rows = data[1::] # these are all the following rows of data
df = pd.DataFrame(data_rows, columns=column_names)

# df
# Out[26]: 
#               Region Alcohol Tobacco
# 0              North    6.47    4.03
# 1          Yorkshire    6.13    3.76
# 2          Northeast    6.19    3.77
# 3      East Midlands    4.89    3.34
# 4      West Midlands    5.63    3.47
# 5        East Anglia    4.52    2.92
# 6          Southeast    5.89    3.20
# 7          Southwest    4.79    2.71
# 8              Wales    5.27    3.53
# 9           Scotland    6.08    4.51
# 10  Northern Ireland    4.02    4.56

df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)
df['Alcohol'].mean() 
# 5.4436363636363634
df['Alcohol'].median() 
# 5.63
# If all numbers occur equally often, stats.mode() will return the smallest number
stats.mode(df['Alcohol']) 
# 4.02

df['Tobacco'].mean() 
# 3.6181818181818186
df['Tobacco'].median() 
# 3.53
stats.mode(df['Tobacco']) 
# 2.71

max(df['Alcohol']) - min(df['Alcohol'])
# 2.4500000000000002
df['Alcohol'].std() 
# 0.79776278087252406
df['Alcohol'].var() 
# 0.63642545454546284

max(df['Tobacco']) - min(df['Tobacco'])
# 1.8499999999999996
df['Tobacco'].std() 
# 0.59070835751355388
df['Tobacco'].var() 
# 0.3489363636363606

print("The mean of the average weekly household spending on Alcohol and Tobacco are " "{} and {} British pounds, respectively.".format(df.Alcohol.mean(), df.Tobacco.mean()))
print("The median of the average weekly household spending on Alcohol and Tobacco are " "{} and {} British pounds, respectively.".format(df.Alcohol.median(), df.Tobacco.median()))
print("The mode of the average weekly household spending on Alcohol and Tobacco are " "{} and {} British pounds, respectively.".format(stats.mode(df.Alcohol)[0][0], stats.mode(df.Tobacco)[0][0]))
print("The range of the average weekly household spending on Alcohol and Tobacco are " "{} and {} British pounds, respectively.".format(max(df.Alcohol) - min(df.Alcohol), max(df.Tobacco) - min(df.Tobacco)))
print("The variance of the average weekly household spending on Alcohol and Tobacco are " "{} and {} British pounds, respectively.".format(df.Alcohol.var(), df.Tobacco.var()))
print("The standard deviation of the average weekly household spending on Alcohol and Tobacco are " "{} and {} British pounds, respectively.".format(df.Alcohol.std(), df.Tobacco.std()))

# Extra, for fun:

# Zscores:
zscore_tobacco = []
for x in df.Tobacco:
	zscore= (x-df.Tobacco.mean())/df.Tobacco.std()
	zscore_tobacco.append(zscore)

zscore_alcohol = []
for x in df.Alcohol:
	zscore= (x-df.Alcohol.mean())/df.Alcohol.std()
	zscore_alcohol.append(zscore)

# Percentile Ranking:




