# Write a script called "chi_squared.py" that loads the data, cleans it, 
# performs the chi-squared test, and prints the result. 
# Push your code to Github and enter the link below.

from scipy import stats
import collections
import pandas as pd
import matplotlib.pyplot as plt

# Load the reduced version of the Lending Club Dataset
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
# Drop null rows
loansData.dropna(inplace=True)

# Count frequency of each 3
freq = collections.Counter(loansData['Open.CREDIT.Lines'])

# Plots Histogram
plt.figure()
plt.bar(freq.keys(), freq.values(), width=1)
plt.title('Open Credit Lines at Lending Club')
plt.xlabel('Open Credit Lines')
plt.ylabel('Count')
plt.savefig('OpenCreditLines_hist.png')
plt.close()

# Chi-squared test
chi, p = stats.chisquare(freq.values())
# Returns following error messages:
# ---------------------------------------------------------------------------
# IndexError                                Traceback (most recent call last)
# <ipython-input-222-e4b44dcfece4> in <module>()
# ----> 1 chi, p = stats.chisquare(freq.values())

# /Users/molliepettit/anaconda/lib/python3.4/site-packages/scipy/stats/stats.py in chisquare(f_obs, f_exp, ddof, axis)
#    3961     """
#    3962     return power_divergence(f_obs, f_exp=f_exp, ddof=ddof, axis=axis,
# -> 3963                             lambda_="pearson")
#    3964 
#    3965 

# /Users/molliepettit/anaconda/lib/python3.4/site-packages/scipy/stats/stats.py in power_divergence(f_obs, f_exp, ddof, axis, lambda_)
#    3818         # is handled without spurious warnings.
#    3819         with np.errstate(invalid='ignore'):
# -> 3820             f_exp = np.atleast_1d(f_obs.mean(axis=axis))
#    3821         if axis is not None:
#    3822             reduced_shape = list(f_obs.shape)

# /Users/molliepettit/anaconda/lib/python3.4/site-packages/numpy/core/_methods.py in _mean(a, axis, dtype, out, keepdims)
#      54     arr = asanyarray(a)
#      55 
# ---> 56     rcount = _count_reduce_items(arr, axis)
#      57     # Make this warning show up first
#      58     if rcount == 0:

# /Users/molliepettit/anaconda/lib/python3.4/site-packages/numpy/core/_methods.py in _count_reduce_items(arr, axis)
#      48     items = 1
#      49     for ax in axis:
# ---> 50         items *= arr.shape[ax]
#      51     return items
#      52 

# IndexError: tuple index out of range

# In [223]: 