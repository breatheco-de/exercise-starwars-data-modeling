import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er
import enum
from sqlalchemy import Integer, Enum

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    size = Column(Integer, nullable=False)
    population = Column(Integer, nullable=False)
    climate = Column(String(250), nullable=False)
    name = Column(String(250), ForeignKey('favourites.favourite_planets'))

class Characters(Base):
    __tablename__ = 'characters'
    name = Column(String(250), ForeignKey('vehicle.pilot'),ForeignKey('favourites.favourite_characters'))
    planet_from = Column(String(250), ForeignKey('planets.name'))
    id = Column(Integer, primary_key=True)
    age = Column(Integer, nullable=False)

class MediaType(enum.Enum):
    png = "png"
    jpg = "jpg"
    gif = "gif"

class Favourites(Base):
    __tablename__ = 'favourites'
    user_id = Column(Integer,ForeignKey('users.user_id'),primary_key=True)
    # user_id = Column(Integer, ForeignKey('users.user_id'))
    favourite_characters = Column(Integer)
    favourite_planets = Column(Integer)
    favourite_vehicles = Column(Integer)
    date_added = Column(DateTime(False))



class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), ForeignKey('favourites.favourite_vehicles'))
    pilot = Column(String(250), nullable=False)
    type = Column(String(250), nullable=False)

class Users(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    type = Column(String(250), nullable=False)

    
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
