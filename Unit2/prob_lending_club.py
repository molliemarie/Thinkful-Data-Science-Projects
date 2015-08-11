# Write a script called "prob_lending_club.py" that reads in the loan data, cleans it, and loads it into a pandas 
# DataFrame. Use the script to generate and save a boxplot, histogram, and QQ-plot for the values in the 
# "Amount.Requested" column. Be able to describe the result and how it compares with the values from the 
# "Amount.Funded.By.Investors". Push your code to Github and enter the link below.

import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

# reads in the loan data
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

# Cleans it
loansData.dropna(inplace=True)

# Boxplot
plt.close()
loansData.boxplot(column='Amount.Requested')
plt.ylabel('Amount Requested ($)')
plt.xlabel(' ')
plt.title('Amount Requested by LendingClub in Dollars')
plt.savefig("amount_requested_boxplot.png")
plt.close()

# histogram
loansData.hist(column='Amount.Requested')
plt.xlabel('Amount Requested ($)')
plt.ylabel('Count')
plt.title('Amount Requested by LendingClub in Dollars')
plt.savefig("amount_requested_hist.png")
plt.close()

# QQ-plot
plt.figure()
graph = stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)
plt.title('Amount Requested by LendingClub in Dollars')
plt.savefig("amount_requested_qqplot.png")
plt.close()

# Describe the result and how it compares with the values from the "Amount.Funded.By.Investors". 

# Boxplots:
# The medians for the two data sets are very close (or equal), 
# and the interquartile ranges are similar, ~6000-17000 vs ~5500-16000 for 
# Amount.Requested and Amount.Funded.By.Investors, respectively.
# Max and min of Amount.Requested and Amount.Funded.By.Investors are 
# ~1000 & ~34000 and ~0 and ~31000, respectively
# Amount.Funded.By.Investors has more outliers (on the high end)
# So, on a case by case basis, it seems the amount funded tends to be slighty less than 
# the amount requested; however, the median ends up being the same

# Histograms:
# The two plots are very similar.
# In both Funded and Requested, ranges ~4500-7000 and ~7000-10500 have highest frequency
# Highest amount Funded is range  ~7000-10500
# High amount Requested is about equal for both ranges
# Plots have same general shape

# QQ-Plot:
# Plots look very similar
# r-squared is 0.9281 and 0.9300 for Requested and Funded, respectively
# Neither are totally normal

