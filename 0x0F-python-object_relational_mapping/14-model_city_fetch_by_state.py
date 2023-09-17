#!/usr/bin/python3
"""This script deletes all State objects with a name
containing the letter a from hbtn_0e_6_usa"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    for state, city in session.query(State, City).filter(
            State.id == City.state_id):
        print(f'{state.name}: ({city.id}) {city.name}')
    session.close()
