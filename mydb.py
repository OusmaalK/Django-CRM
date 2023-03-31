import mysql.connector

dataBase = mysql.connector.connect(
	host='localhost',
	user='root',
	passwd='Root2023@'
)

#prepare a cursor object

cursorObject=dataBase.cursor()

#Cretate a database

cursorObject.execute("CREATE DATABASE capitalnet")

print("All done !")