#!/usr/bin/python3
"""
Class Definition of a `State` and an instance
`Base = declarative_base()`
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """ Represents a state for a MySQL database.
    __tablename__(str): The name of the MySQL table (`states`)
    id (sqlalchemy.Integer): The state's id attribute
    name (sqlalchemy.String): The state's name attribute
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
