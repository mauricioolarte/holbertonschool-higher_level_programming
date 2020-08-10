#!/usr/bin/python3
"""Start link class to table in database
"""
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship


class City(Base):
    """ this create a table states """
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, nullable=False,
                primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
    states = relationship(State)
