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

# Extracting data from a notebook ************
# specify first row through last row and then
# first column to last column wanted. EX:
# df7=pandas.read_json("myFile.json")
# df7.loc["myID":"mySecondID","myColumn":"mySecondColumn"]
# or more commonly
# df7.iloc[1:3,1:3]

# How to drop/delete
# df7=df7.drop("myRow", <number of column or leave blank>)

# Pandas Geocoding==============
# from geopy.geocoders import ArcGIS
# nom = ArcGIS()
# nom.geocode("122 Street, City, state zip")
# storing in variable
# n=nom.geocode("122 street, city, state zip")
# print(n.lattitude)