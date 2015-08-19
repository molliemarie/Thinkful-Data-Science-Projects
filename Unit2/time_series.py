# Write a script called "time_series.py" to load, clean, and plot the data. 
# Have the script print out whether there are autocorrelated structures in 
# the data. Push the code to Github and include a link below.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
loanStats = pd.read_csv('/Users/molliepettit/Desktop/Data Science/Thinkful/Projects/Unit2/LoanStats3b.csv', header=1, low_memory=False)

# converts string to datetime object in pandas:
loanStats['issue_d_format'] = pd.to_datetime(loanStats['issue_d']) 
dfts = loanStats.set_index('issue_d_format') 
year_month_summary = dfts.groupby(lambda x : x.year * 100 + x.month).count()
loan_count_summary = year_month_summary['issue_d']


# Plot the loan data (loan_count_summary in from the previous assignment). 
# Is the series stationary? 
# If not, what would you do to transform it into a stationary series?

plt.plot(loan_count_summary)

# The series is increasing with time, so no, it's not stationary
# We can differntiate it toget another time series that might be stationary in nature. 

loan_count_summary_diff = loan_count_summary.diff()
loan_count_summary_diff = loan_count_summary_diff.fillna(0)

plt.plot(loan_count_summary_diff)

#To remove negative values, add 316 to all values.
loan_count_summary_diff = loan_count_summary_diff + 316

# By dividing by the maximum value, we smooth out the plot. The graph now plots between 0 and 1. 

loan_count_summary_diff = loan_count_summary_diff/max(loan_count_summary_diff)
plt.plot(loan_count_summary_diff)
plt.savefig('LoanCountSummaryDiff.png')

# Plot ACF
plt.close()
sm.graphics.tsa.plot_acf(loan_count_summary_diff)
plt.savefig('ACF_loancount.png')

# Plot PACF
plt.close()
sm.graphics.tsa.plot_pacf(loan_count_summary_diff)
plt.savefig('PACF_loancount.png')

# Are there any autocorrelated structures in the series? 
# How would you have a model address these structures?

# Ask Shubhabrata to discuss this.

