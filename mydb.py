import mysql.connector


dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    password ='236018br#'

)

#prepare a cursor object
cursorObject = dataBase.cursor()

#create a database

cursorObject.execute("CREATE DATABASE Trillion")

