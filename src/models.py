import os
import sys
import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    username = Column(String(250))
    password = Column(String(250))

class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    mass = Column(Integer)
    height = Column(Integer)
    hair_color = Column(String(100))
    eye_color = Column(String(100))
    birth_year = Column(DateTime, default=datetime.datetime.utcnow)
    gender = Column(String(30))
    homeworld = Column(String(50))
    species = Column(String(50))
    vehicles = Column(String(50))
    starships = Column(String(50))

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    diameter = Column(Integer)
    climate = Column(String(100))
    gravity = Column(String(100))
    terrain = Column(String(100))
    surface_water = Column(Integer)
    population = Column(Integer)

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')