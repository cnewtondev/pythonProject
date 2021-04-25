#install pandas pip3.9 install pandas

# We will also install Ipython
# (IPython is just like the standard shell 
# you get when you run Python, but IPython 
# provides better printing for large text.)


#HOW TO CREATE PANDAS DATAFRAME
#cmd: ipython
# In [1]: import pandas

# In [2]: df=pandas.DataFrame([[2,4,6],[10,20,30]])
#============================================
# In [5]: df=pandas.DataFrame([[2,4,6],[10,20,30]],columns=["Price","Age","Value"])

# In [6]: df
# Out[6]:
#    Price  Age  Value
# 0      2    4      6
# 1     10   20     30
#================================================

# In [7]: df=pandas.DataFrame([[2,4,6],[10,20,30]],columns=["Price","Age","Value"], index=["First", "Secon
#    ...: d"])

# In [8]: df
# Out[8]:
#         Price  Age  Value
# First       2    4      6
# Second     10   20     30

#==================================================
# In [9]: df2=pandas.DataFrame([{"Name":"Jack", "UserName":"YourName101"},{"Name":"Yodal", "UserName":"Yoda"}])

# In [10]: df2
# Out[10]:
#     Name     UserName
# 0   Jack  YourName101
# 1  Yodal    Yoda

# ACCESSING PANDAS DATAFRAME METHODS===============
# cmd: dir(df2)
# #EX: 
# In [13]: df.mean()
# Out[13]:
# Price     6.0
# Age      12.0
# Value    18.0
# dtype: float64