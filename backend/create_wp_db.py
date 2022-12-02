import mysql.connector

wp_db = mysql.connector.connect(host="localhost", user="root", password="QWer1234")
my_cursor = wp_db.cursor()
my_cursor.execute("CREATE DATABASE wp_db")

my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)
