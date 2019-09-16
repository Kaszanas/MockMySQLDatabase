from model import *
import time

def populate_ids_with_ids(session, i):
    session.add(UserID(id=i+1))

def populate_table_with_data(session, date, foreign_id, name_of_event, money=None):
    session.add(Tables(userID=foreign_id, eventDate=date , eventName=name_of_event, price=money))

def str_time_prop(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))

def random_date(start, end, prop):
    return str_time_prop(start, end, '%Y/%m/%d', prop)