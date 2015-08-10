import numpy as np 
import scipy.stats as stats
import matplotlib.pyplot as plt
import collections

# Define data
x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]

# Frequencies:
# Count number of instances per number
c = collections.Counter(x)
# calculate the number of instances in the list
count_sum = sum(c.values())
# Determine frequency of each value
# NOTE: c.iteritems no longer exists in Python 3. Instead, just c.items is used.
for k,v in c.items():
  print("The frequency of number " + str(k) + " is " + str(float(v) / count_sum))

# In case there are already plots open.
plt.close()

# Create and save boxplot
bp = plt.boxplot(x)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Creative Boxplot Title')
plt.savefig("prob_boxplot.png")
plt.close()

# Create and save histogram
import matplotlib.pyplot as plt
plt.hist(x, histtype='bar')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Creative Histogram Title')
plt.savefig("prob_hitogram.png")
plt.close()

 # Create and save QQ-Plot
graph1 = stats.probplot(x, dist="norm", plot=plt)
plt.savefig("prob_qqplot.png")

