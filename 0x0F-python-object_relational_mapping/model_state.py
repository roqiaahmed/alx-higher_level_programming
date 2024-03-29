#!/usr/bin/python3
"""Start link class to table in database
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from model_city import City

Base = declarative_base()

class State (Base):
    """Class representing the states table"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
