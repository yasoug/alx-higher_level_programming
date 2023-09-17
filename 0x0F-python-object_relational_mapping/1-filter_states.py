#!/usr/bin/python3
"""
Script lists all states with a name starting with N from hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    database = MySQLdb.connect(host="localhost",
                               user=argv[1], port=3306,
                               password=argv[2], database=argv[3])
    cursor = database.cursor()
    cursor.execute("SELECT * FROM states WHERE NAME LIKE 'N%' ORDER BY id ASC")
    for row in cursor.fetchall():
        if row[1][0] == 'N':
            print(row)
    cursor.close()
    database.close()
