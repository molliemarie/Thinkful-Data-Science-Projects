import pandas as pd
import statsmodels.api as sm
from math import exp

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
ind_vars =['Intercept', 'Amount.Requested', 'FICO.Score']

# Define the logistic regression model.
x = loansData_clean[ind_vars]
y = loansData_clean['IR_TF']
logit = sm.Logit(y,x)

# Fit the model.
result = logit.fit()

# Get the fitted coefficients from the results.
coeff = result.params
print(coeff)

# Using these coefficients, what is the linear part of our predictor?
# interest_rate = -60.125 + 0.087423(FicoScore) - 0.000174(LoanAmount)

# What is our logistic function?
# p(x) = 1/(1 + e^(intercept + 0.087423(FicoScore) − 0.000174(LoanAmount))

# Write a function called logistic_function that will take a FICO Score 
# and a Loan Amount of this linear predictor, and return p. (Try not to 
# 	hardcode any values if you can! Hint: pass the coefficients object 
# 	to the function as an argument.)

def logistic_function(fico_score, loan_amt, coeff):
	prob= 1/(1 + exp(coeff[0] + coeff[2]*fico_score + coeff[1]*loan_amt))
	if prob > 0.7:
		p = 1
	else: 
		p = 0
	return prob, p

# Determine the probability that we can obtain a loan at ≤12% Interest 
# for $10,000 with a FICO score of 720 using this function.
logistic_function(720, 10000, coeff)
# Out[123]: (0.253621411048487, 0)

prob = logistic_function(720, 10000,coeff)[0]
decision = logistic_function(720, 10000,coeff)[1]

# Is p above or below 0.70?
# Do you predict that we will or won't obtain the loan?
# The probability is WELL below 0.71 and we will not obtain the loan.

#Now think critically, does your prediction make sense given the data? 
# Try plotting the data to see if you can see the prediction visually. 
# If you cannot find the correlation visually, you might have to re-evaluate 
# your logistic function. An example plot can be seen here, created by one 
# of our data science mentors, which compares two different equations for 
# the logistic regression. Which one makes more sense?

# The blue line makes more sense, because as FICO scores decrease when loan 
# amount stays the same, the probability of being granted your loan goes up

Fico = range(550, 950, 10)
p_plus = []
# p_minus = []
p = []
for j in Fico:
    p_plus.append(1/(1+exp(coeff[0]+coeff[2]*j+coeff[1]*10000)))
    # p_minus.append(1/(1+exp(-coeff[0]-coeff[2]*j-coeff[1]*10000)))
    p.append(logistic_function(j, 10000,coeff)[1])

plt.plot(Fico, p_plus, label = 'p(x) = 1/(1+exp(b+mx))', color = 'blue')
plt.hold(True)
# plt.plot(Fico, p_minus, label = 'p(x) = 1/(1+exp(-b-mx))', color = 'green')    
# plt.hold(True)
plt.plot(Fico, p, 'ro', label = 'Decision for 10000 USD')
plt.legend(loc='upper right')
plt.xlabel('Fico Score')
plt.ylabel('Probability and decision, yes = 1, no = 0')
plt.save('Fico_logisticRegression.png')

# If you're feeling really adventurous, you can create a new function pred 
# to predict whether or not we'll get the loan automatically.

def pred(fico_score, loan_amt, coeff):
	prob= 1/(1 + exp(coeff[0] + coeff[2]*fico_score + coeff[1]*loan_amt))
	if prob > 0.7:
		print('You will likely not be granted your requested loan')
	else: 
		print("You will likely be granted your requested loan")
	return prob, p
