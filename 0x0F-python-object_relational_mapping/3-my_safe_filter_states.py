#!/usr/bin/python3
"""
This script takes in an argument and displays all values in the states table
where name matches the argument, safe from MySQL injections
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    database = MySQLdb.connect(host="localhost",
                               user=argv[1], port=3306,
                               password=argv[2], database=argv[3])
    state = argv[4]
    cursor = database.cursor()
    cursor.execute("SELECT * FROM states WHERE NAME = %s", (state,))
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    database.close()
