#!/usr/bin/python3
"""
This script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    database = MySQLdb.connect(host="localhost",
                               user=argv[1], port=3306,
                               password=argv[2], database=argv[3])
    cursor = database.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name \
                   FROM states, cities \
                   WHERE cities.state_id=states.id")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    database.close()
