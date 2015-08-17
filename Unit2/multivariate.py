import pandas as pd
import statsmodels.api as sm
from math import exp

# Load Data
loansData = pd.read_csv('/Users/molliepettit/Desktop/Data Science/Thinkful/Projects/Unit2/loansData_clean.csv')

# Use income (annual_inc) to model interest rates (int_rate)

	# Values from before:
loan_amt = loansData['Amount.Requested']
loan_amt[np.isnan(loan_amt)] = 0
fico = loansData['FICO.Score']
fico[np.isnan(fico)] = 0

	# New Values
int_rate = loansData['Interest.Rate']
intrate[np.isnan(intrate)] = 0
monthly_inc = loansData['Monthly.Income']
monthly_inc[np.isnan(monthly_inc)] = 0
loansData['Annual.Income'] = loansData['Monthly.Income']*12
annual_inc = loansData['Annual.Income']


# Add home ownership (home_ownership) to the model.
home_ownership = loansData['Home.Ownership']
home_ownership = [4 if x == 'OWN' else 3 if x == 'MORTGAGE' else 2 if x == 'RENT' else 1 if x == 'OTHER' else 0 for x in home_ownership]

y = np.matrix(int_rate).transpose()
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loan_amt).transpose()
x3 = np.matrix(home_ownership).transpose()
x4 = np.matrix(annual_inc).transpose()

x = np.column_stack([x1,x2,x3])

X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()
f.summary()

print('Intercept: ', f.params[0])
print('Coefficients: ', f.params[1:])
print('P-Values: ', f.pvalues)
print('R-Squared: ', f.rsquared)

# Intercept:  0.729618469628
# Coefficients:  [ -8.82804621e-04   2.11264610e-06  -7.63593229e-04]
# P-Values:  [  0.00000000e+000   0.00000000e+000   1.39662984e-202   3.28018279e-001]
# R-Squared:  0.65676423697


# Add home_ownership and annual_inc into the model

x2 = np.column_stack([x1,x2,x3,x4])

# Create Multivariate model
X = sm.add_constant(x2)
model = sm.OLS(y,X)
g = model.fit()
# results summary
g.summary()

coeffg = g.params
b = coeffg[0]
ficoCoeff = coeffg[1]
loanamtCoeff = coeffg[2]
annualIncCoeff = coeffg[3]
homeOwnCoeff = coeffg[4]


print('Intercept: ', g.params[0])
print('Coefficients: ', g.params[1:])
print('P-Values: ', g.pvalues)
print('R-Squared: ', g.rsquared)

# Intercept:  0.726903915495
# Coefficients:  [ -8.77018478e-04   2.23439410e-06  -4.81820562e-04  -5.30116970e-08]
# P-Values:  [  0.00000000e+000   0.00000000e+000   6.98428848e-197   5.36556771e-001
#    2.44565763e-006]
# R-Squared:  0.659806521568


#Does that affect the significance of the coefficients in the original 
# model? + Try to add the interaction of home ownership and incomes as a term. 
# How does this impact the new model?


#  R squared is nearly the same for both models


