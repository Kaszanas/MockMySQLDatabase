import datetime
import os
import time
import datetime
import logging
import random
import math

from tqdm import tqdm
from sqlalchemy import UniqueConstraint, literal
from sqlalchemy.orm import query
from database_connection import create_engine
from settings import CONNECTION_STRING, DATABASE_NAME

from model import *
import functions

logger = logging.getLogger()

if __name__ == '__main__':
    logging.basicConfig()
    engine = create_engine(CONNECTION_STRING, DATABASE_NAME, True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine, autoflush=False)
    session = Session()

    possible_events = ['Program-Turned-On', 'Performed-Transaction']

    # Creating 1000 users
    n_users = 1000
    for i in tqdm(range(n_users)):
        functions.populate_ids_with_ids(session, i)

    session.commit()
       
    # Looking over all registered Users to generate events

    q = session.query(UserID)

    for element in tqdm(range(n_users)):
        date_0 = functions.random_date('2019/08/01', '2019/09/01', random.random())
        functions.populate_table_with_data(session, date_0, q[element].id, 'New-User')

    session.commit()

    q0 = session.query(Tables.userID, Tables.eventDate)
    q0 = q0.all()

    # Taking into consideration that a New-Users might buy something right after starting the program
    for i in tqdm(range(n_users)):
            if random.randint(0,1) == 1:

                random_user = random.randint(0, 999)
                min_to_max_date = functions.random_date(q0[random_user][1].strftime('%Y/%m/%d'), '2019/09/01', random.random())

                possible_price = round(random.uniform(1,100), 1) 
                functions.populate_table_with_data(session, min_to_max_date, q0[random_user][0], possible_events[1], possible_price)

                session.commit()

    session.commit()

    q0 = session.query(Tables.userID, Tables.eventDate)
    q0 = q0.all()

    for s in tqdm(range(n_users * 25)):
        # I throw in an assumption that a User can perform between 0 and 25 actions during his time within specified time range.

        # Randomly choosing if User decided to log in.
        if random.randint(0,1) == 1:

            random_user = random.randint(0, 999)

            # I make sure that user cannot log in before he is New-User by selecting the user via query.
            min_to_max_date = functions.random_date(q0[random_user][1].strftime('%Y/%m/%d'), '2019/09/01', random.random())
            functions.populate_table_with_data(session, min_to_max_date, q0[random_user][0], possible_events[0])

            session.commit()

            # Randomly deciding if User decided to perform a transaction and pay a random amount between 1 and 100
            if random.randint(0,1) == 1:
                possible_price = round(random.uniform(1,100), 1) 
                functions.populate_table_with_data(session, min_to_max_date, q0[random_user][0], possible_events[1], possible_price)

                session.commit()
