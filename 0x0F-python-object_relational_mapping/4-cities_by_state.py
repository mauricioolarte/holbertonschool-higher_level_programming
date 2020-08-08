#!/usr/bin/python3
""" this module if a query whit join """
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    curs = db.cursor()
    curs.execute("select cities.id, cities.name, states.name from\
                 cities join states on cities.state_id=states.id")
    rows = curs.fetchall()
    for row in rows:
        print(row)
