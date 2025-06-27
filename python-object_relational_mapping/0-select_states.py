#!/usr/bin/python3

import sys
import MySQLdb


username = sys.argv[1]
password = sys.argv[2]
database_name = sys.argv[3]

database = MySQLdb.connect(
    host="localhost",
    user=username,
    passwd=password,
    port=3306,
    database=database_name
)

cursor = database.cursor()
cursor.exectute("SELECT * FROM states ORDERBY id ASC")
for row in cursor.fetchall():
    print(row)
cursor.close()
database.close()
