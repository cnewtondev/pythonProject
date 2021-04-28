# download anaconda3 so you can use their terminal.
# create new folder or have a present folder. 
# cd into folder and then dropmenu > python3

# you can view contents of what is inside by fallowing cmd:
# import os
# os.listdir()

# to actually read a csv file you can use fallowing cmd:
# import pandas
# df1=pandas.read_csv("supermarkets.csv")
# Note: you can also do this with different data 
# set files such as json!
# Remember when opening excel(xlsx) files that you 
# can specify specific page numbers like so:
# df3=pandas.read_excel("supermarkets.xlsx",sheet_name=0)
# df3
# For txt files you actually use the pandas_csv cmd.
# this is due to "character"seperators. EX:
# df4=pandas.read_csv("supermarkets-commas.txt")
# df4