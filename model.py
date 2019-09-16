from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class UserID(Base):
    __tablename__ = 'userids'

    # Columns
    id = Column(Integer, primary_key=True, autoincrement=False)

    # Relationships
    table = relationship('Tables', back_populates='userids')

class Tables(Base):
    __tablename__ = 'table'

    # Columns
    own_id = Column(Integer, primary_key=True, autoincrement=True)
    userID = Column(Integer, ForeignKey('userids.id'))
    eventDate = Column(DateTime)
    eventName = Column(String(length=128))
    price = Column(Float)

    # Relationships
    userids = relationship('UserID', back_populates='table')