import pandas as pd
import statsmodels.api as sm

# Load Data
loansData_clean = pd.read_csv('/Users/molliepettit/Desktop/Data Science/Thinkful/Projects/Unit2/loansData_clean.csv')

# Add a column to your dataframe indicating whether the interest rate is 
# < 12%. This would be a derived column that you create from the interest 
# rate column. You name it IR_TF. It would contain binary values, i.e.'0' 
# when interest rate < 12% or '1' when interest rate is >= 12%
loansData_clean['IR_TF'] = (loansData_clean['Interest.Rate'] < 0.12)

# Do some spot checks to make sure that it worked.
# loansData_clean[loansData_clean['Interest.Rate'] == .10].head() # should all be True
# loansData_clean[loansData_clean['Interest.Rate'] == .2198].head() # should all be False

# Statsmodels needs an intercept column in your dataframe, 
# so add a column with a constant intercept of 1.0.
loansData_clean['Intercept'] = 1

# Create a list of the column names of our independent variables, 
# including the intercept, and call it ind_vars.
# loansData_clean['ind_vars'] = list(loansData_clean.columns.values)
ind_vars =list(loansData_clean.columns.values)

# Define the logistic regression model.
logit = sm.Logit(loansData_clean['IR_TF'], ind_vars)

# # Fit the model.
# result = logit.fit()

# # Get the fitted coefficients from the results.
# coeff = result.params
# print coeff