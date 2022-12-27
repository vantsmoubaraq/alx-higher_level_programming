#!/usr/bin/python3
"""
Lists all `State` Objects and corresponding `City`
Objects contained in the database `hbtn_0e_101_usa
Usage: ./101-relationship_states_cities_list.py <mysql username>
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

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).order_by(State.id).all()
    for row in result:
        print("{}: {}".format(row.id, row.name))
        for city in row.cities:
            print("    {}: {}".format(city.id, city.name))
