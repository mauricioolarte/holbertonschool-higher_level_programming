#!/usr/bin/python3
""" this module if for a query whit argument from comand line"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    curs = db.cursor()
    curs.execute("SELECT * FROM states WHERE binary name = '{}'\
                 ORDER BY id ASC ".format(sys.argv[4]))
    rows = curs.fetchall()
    for row in rows:
        print(row)
