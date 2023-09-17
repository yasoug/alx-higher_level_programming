#!/usr/bin/python3
"""
This script takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    database = MySQLdb.connect(host="localhost",
                               user=argv[1], port=3306,
                               password=argv[2], database=argv[3])
    state = argv[4]
    cursor = database.cursor()
    cursor.execute("SELECT cities.name FROM cities, states \
                   WHERE cities.state_id = states.id \
                   AND states.name LIKE %s", (state,))
    print(", ".join(["{:s}"
                     .format(row[0]) for row in cursor.fetchall()]))
    cursor.close()
    database.close()
