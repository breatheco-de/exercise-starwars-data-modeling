import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey("characters.id"))    
    planet_id = Column(Integer, ForeignKey("planets.id"))    
    user_id = Column(Integer, ForeignKey("user.id"))    

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
