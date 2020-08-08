#!/usr/bin/python3
""" this file is for a query inserting a parameter"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost',
                         port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    curs = db.cursor()
    curs.execute("SELECT * FROM states WHERE name LIKE BINARY\
                 'N%' ORDER BY id ASC")
    rows = curs.fetchall()
    for row in rows:
        print(row)
