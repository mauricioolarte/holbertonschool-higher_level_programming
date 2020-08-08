#!/usr/bin/python3
""" this module make a query whit arguments from command line"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    curs = db.cursor()
    curs.execute("select cities.name from cities join states on\
                 cities.state_id=states.id\
                 where states.name = %s", (sys.argv[4],))
    rows = curs.fetchall()
    for row in range(0, len(rows)):
        if row == 0:
            print("{}".format(rows[row][0]), end='')
        else:
            print(", {}".format(rows[row][0]), end='')
    print()
