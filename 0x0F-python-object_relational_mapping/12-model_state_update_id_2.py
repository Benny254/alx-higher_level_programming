#!/usr/bin/python3
"""Updates the name of a State object in the database"""

if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    # Create the database engine
    engine = create_engine("mysql://{}:{}@localhost/{}".
                           format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query the State object with id = 2 and change its name to 'New Mexico'
    state_to_update = session.query(State).filter_by(id=2).first()
    if state_to_update:
        state_to_update.name = 'New Mexico'
        session.commit()
