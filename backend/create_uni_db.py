import mysql.connector

uni_db = mysql.connector.connect(host="localhost", user="root", password="QWer1234")
my_cursor = uni_db.cursor()
my_cursor.execute("CREATE DATABASE uni_db")

my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)
