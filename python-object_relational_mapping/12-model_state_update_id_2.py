#!/usr/bin/python3
"""Changes the name of a State object."""

import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]
        ),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

    session = Session(engine)

    state_update = session.query(State).where(State.id.ilike(2))
    state = state_update.one()
    if state:
        state.name = 'New Mexico'
        session.commit()
