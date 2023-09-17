#!/usr/bin/python3
"""Start link class to table in database
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class City (Base):
    """Class representing the cities table"""
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
