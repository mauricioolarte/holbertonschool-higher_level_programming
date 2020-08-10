#!/usr/bin/python3
"""Start link class to table in database
"""
from model_city import City
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()


class State(Base):
    """ this create a table states """
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, nullable=False,
                primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = relationship(City, backref="state")
