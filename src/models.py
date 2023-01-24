import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class People(Base):
    __tablename__ = 'people'
    # Here we define columns for the table people
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    birth_year = Column(String(250), nullable=False)
    homeworld = Column(String(250), nullable=False)
    starship = Column(String(250), nullable=False)


class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table planets.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    population = Column(String(250), nullable=False)
    gravity = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)

class Starships(Base):
    __tablename__ = 'starships'
    # Here we define columns for the table people
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    starship_class = Column(String(250), nullable=False)
    passengers = Column(String(250), nullable=False)

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table people
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)

class Likes(Base):
    __tablename__ = 'likes'
    # Here we define columns for the table people
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    people_id = Column(Integer, ForeignKey('people.id'))
    people = relationship(People)
    planets_id = Column(Integer, ForeignKey('planets.id'))
    planets = relationship(Planets)
    vehicles_id = Column(Integer, ForeignKey('vehicles.id'))
    vehicles = relationship(Vehicles)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
