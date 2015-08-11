import pandas as pd
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

# loansData['FICO.Range'][0:5]
# Returns as follow:
# 81174    735-739
# 99592    715-719
# 80059    690-694
# 15825    695-699
# 33182    695-699

# Split into numbers - will return in form [###, ###]
cleanFICORange = loansData['FICO.Range'].map(lambda x: x.split('-'))

# Results:
# >>> cleanFICORange[0:5]
# 81174    [735, 739]
# 99592    [715, 719]
# 80059    [690, 694]
# 15825    [695, 699]
# 33182    [695, 699]
# Name: FICO.Range, dtype: object
# >>> cleanFICORange[0:5].values[0]
# ['735', '739']
# >>> type(cleanFICORange[0:5].values[0])
# <type 'list'>
# >>> cleanFICORange[0:5].values[0][0]
# '735'
# >>> type(cleanFICORange[0:5].values[0][0])
# <type 'str'>

# We have a string inside a list. Need to convert each string to integer
# To do this, we use a list comprehension
# The "[0]" at the end makes it so that we only choose the first element
cleanFICOScore = cleanFICORange.map(lambda x: [int(n) for n in x][0])

# Results:
# print(cleanFICORange.head(5))
# 81174    735
# 99592    715
# 80059    690
# 15825    695
# 33182    695
# Name: FICO.Range, dtype: int64

# To understand better, check out: http://carlgroner.me/Python/2011/11/09/An-Introduction-to-List-Comprehensions-in-Python.html

loansData['FICO.Score'] = cleanFICOScore
# print(loansData['FICO.Score'].head(5))
# 81174    735
# 99592    715
# 80059    690
# 15825    695
# 33182    695
# Name: FICO.Score, dtype: int64



# FOR ANOTHER WAY TO DO THIS, following was posted below tutorial:
# I accomplished the entire process with 4 four lines of codes using list comprehensions:

# import pandas as pd
# #read data into dataframe
# loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

# #remove % symbol from interest rate and convert to float
# loansData['Interest.Rate'] = [float(interest[0:-1])/100 for interest in loansData['Interest.Rate']]

# #remove "month" at the end of loan length and convert to integer
# loansData['Loan.Length'] = [int(length[0:-7]) for length in loansData['Loan.Length']]

# #create a new column called Fico Score with lower limit value
# loansData['FICO.Score'] = [int(val.split('-')[0]) for val in loansData['FICO.Range']]




