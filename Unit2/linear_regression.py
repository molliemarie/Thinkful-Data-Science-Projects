import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')


# FICO DATA

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

# Assign cleaned score to new column called "FICO.Score"
loansData['FICO.Score'] = cleanFICOScore
# print(loansData['FICO.Score'].head(5))
# 81174    735
# 99592    715
# 80059    690
# 15825    695
# 33182    695
# Name: FICO.Score, dtype: int64

# Histogram
plt.figure()
p = loansData['FICO.Score'].hist()
plt.savefig('FicoScore_hist.png')
plt.close()

# Scatterplot matrix
a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10), diagonal='hist')
plt.savefig('FicoScore_ScatterMatrix.png')
plt.close()


# CLEAN INTEREST RATE DATA
clean_ir = loansData["Interest.Rate"].map(lambda x: round(float(x.rstrip("%"))/100, 4))
loansData["Interest.Rate"] = clean_ir

# CLEAN LOAN LENGTH DATA
clean_loanLength = loansData["Loan.Length"].map(lambda x: float(x.rstrip("months")))
loansData["Loan.Length"] = clean_loanLength

# LINEAR REGRESSION!

# Linear regression model: 
# InterestRate = b + a1(FICOScore) + a2(LoanAmount)

intrate = loansData['Interest.Rate']
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Score']

# Create y and x variables
# The dependent variable
y = np.matrix(intrate).transpose()
# The independent variables shaped as columns
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()
# put the two columns together to create an input matrix 
x = np.column_stack([x1,x2])

# Create linear model
X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()
# results summary
f.summary()
  
  