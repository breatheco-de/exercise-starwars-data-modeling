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
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('user.id'))
    id_card = Column(Integer, ForeignKey('character.id'))
    name = Column(String(250), ForeignKey('character.name'))

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    image = Column(String(250))
    name_planet = Column(String(250))
    population  = Column(String(250))
    terrain = Column(String(250))

class Planet_Card(Base):
    __tablename__ = 'planet_card'
    id = Column(Integer, primary_key=True)
    id_planet_card = Column(Integer, ForeignKey('planet.id'))
    image = Column(String(250))
    name = Column(String(250), ForeignKey('planet.name_planet'))
    description = Column(String(500))

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    image = Column(String(250))
    name = Column(String(250))
    gender = Column(String(250))
    eye_color = Column(String(250))
    hair_color   = Column(String(250))

class Character_Card(Base):
    __tablename__ = 'character_card'
    id = Column(Integer, primary_key=True)
    character = relationship(Character)
    id_character = Column(Integer, ForeignKey('character.id'))
    #image = Column(String(250)) no se tendrian que poner porque salen de la relacion con la character, correcto?
    #name = Column(String(250))
    description = Column(String(500))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
