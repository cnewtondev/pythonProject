#install library to allow python to interact with a MySQL database
# pip3 install mysql-connector-python
import mysql.connector

con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student", 
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

cursor = con.cursor()

word = raw_input("Please Enter A Word: ")

queryOne = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s' " % word)
results = cursor.fetchall()

if results:
    for result in results:
        print(result[1])
else:
    print("No word found")