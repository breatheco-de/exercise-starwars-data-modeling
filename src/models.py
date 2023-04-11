import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
   # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    fisrt_name = Column(String(250))
    last_name = Column(String(250))
    email = Column(String(250))

class Favorites(Base):
    __tablename__ = 'favorites'
    user_id = Column(Integer, ForeignKey('user.id'))
    card_id = Column(Integer, ForeignKey('dni.global_id'))
    name_card = Column(String(250), primary_key=True)
    category = Column(String(250))

class Dni(Base):
    __tablename__ = 'dni'
    character_id = Column(Integer, ForeignKey('character.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    global_id = Column(Integer, primary_key=True)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    image = Column(String(250))
    name_planet = Column(String(250))
    population  = Column(String(250))
    terrain = Column(String(250))

class Planet_Card(Base):
    __tablename__ = 'planet_card'
    id_planet_card = Column(Integer, ForeignKey('planet.id'))
    image = Column(String(250))
    name_planet = Column(String(250), primary_key=True)
    description = Column(String(500))
    climate = Column(String(250))
    population = Column(Integer)
    oribit_period = Column(Integer)
    rotation_period = Column(Integer)
    diameter = Column(Integer)

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    image = Column(String(250))
    name = Column(String(250))
    gender = Column(String(10))
    eye_color = Column(String(250))
    hair_color   = Column(String(250))

class Character_Card(Base):
    __tablename__ = 'character_card'
    id_character = Column(Integer, ForeignKey('character.id'))
    image_character = Column(String(10))
    name_character = Column(String(20), primary_key=True)
    description = Column(String(500))
    birthday = Column(String(10))
    gender = Column(String(10))
    height = Column(Integer)
    eye_color = Column(String(10))
    skin_color = Column(String)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
