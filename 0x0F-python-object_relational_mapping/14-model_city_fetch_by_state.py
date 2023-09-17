#!/usr/bin/python3
"""Lists states"""

from sys import argv
from sqlalchemy import (create_engine)
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for state, city in session.query(State, City).filter(City.state_id == State.id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.commit()
    session.close()
