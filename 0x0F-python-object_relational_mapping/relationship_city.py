#!/usr/bin/python3
"""
Class Definition of a `City` and an instance
`Base = declarative_base()`
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from relationship_state import Base, State
from sqlalchemy import ForeignKey


class City(Base):
    """ Represents cities for a MySQL database.
    __tablename__(str): The name of the MySQL table (`cities`)
    id (sqlalchemy.Integer): The state's id attribute
    name (sqlalchemy.String): The state's name attribute
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
