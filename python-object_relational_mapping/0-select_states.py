import MySQLdb


username = "mysql username"
password = "mysql password"
database = "mysql database"

db = MySQLdb.connect(
    host="localhost",
    user=username,
    password=password,
    port=3306,
    database="database_name"
)

cursor = database.cursor()
cursor.exectute("SELECT * FROM states ORDERBY id ASC")
for row in cursor.fetchall():
    print(row)