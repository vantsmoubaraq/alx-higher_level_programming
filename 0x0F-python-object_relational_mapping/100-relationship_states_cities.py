#!/usr/bin/python3
"""
Creates `State` California with `City` San Francisco
from database `hbtn_0e_100_usa
Usage: ./10-mode_state_my_get.py <mysql username>
                                 <mysql password>
                                 <database name>
                                 <name searched>
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City, Base
from relationship_state import State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    newState = State(name='California')
    newState.cities = [City(name='San Francisco')]
    session.add(newState)
    session.commit()
