#!/usr/bin/python3
"""
alchimy
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb//{}:{}@localhost:3306/{}'.format(user, passwd, db),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).order_by(State.id).all()

for state in result:
    print("{}: {}".format(state.id, state.name))
