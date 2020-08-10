#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker, join, query
from sqlalchemy import (create_engine)
from sqlalchemy import asc

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).join(City).order_by(cities.id.asc())
    for row in query:
        for city in row.states:
            print("{}: ({}) {}".format(states.name, cities.id, cities.name))
