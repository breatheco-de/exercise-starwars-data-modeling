import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique = True)
    

class Favourites(Base):
    __tablename__ = 'favourites'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user_fav_planet = Column(Integer, ForeignKey('planets.id'))
    user_fav_characters = Column(Integer, ForeignKey('characters.id'))


class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table planets.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(250), nullable = False)
    favourites = relationship(Favourites)


class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table character.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    character_name = Column(String(250), nullable = False)
    favourites = relationship(Favourites)    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')