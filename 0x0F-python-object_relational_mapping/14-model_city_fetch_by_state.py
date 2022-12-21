#!/usr/bin/python3 

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(City, State).join(State, State.id==City.state_id).order_by(City.id).all()
    
    for city, state in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
