#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cur = db.cursor()
    query = ("""SELECT * FROM states WHERE BINARY name = '{}'
        ORDER BY id ASC""".format(state))
    cur.execute(query)
    rows = cur.fetchall()

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
