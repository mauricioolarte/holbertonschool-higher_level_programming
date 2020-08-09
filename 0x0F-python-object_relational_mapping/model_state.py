#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
import sqlalchemy
#from model_state import Base, State
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           sys.argv[1], sys.argv[2],
                           sys.argv[3]), pool_pre_ping=True)
#    Base.metadata.create_all(engine)
    Base = declarative_base()
    class State(Base):
        __tablename__ = 'states'

        id = Column(Integer, autoincrement=True, nullable=False, unique=True,
                    primary_key=True)
        name = Column(String(128), nullable=False)

    Base.metadata.create_all(engine)
