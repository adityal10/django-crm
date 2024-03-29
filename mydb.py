import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='aditya'
)

# prepare a cursor object
cursorobj = database.cursor()

#create a database
cursorobj.execute('CREATE DATABASE crm')

print("all done")