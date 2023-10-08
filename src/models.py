from sqlalchemy import Column, ForeignKey, Integer, String, Float, Boolean
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
    full_name = Column(String(250), nullable=False, unique=True)
    email = Column(String(250), nullable=False) 
    password = Column(String(250), nullable=False) 
    subscription_date = Column(String(250), nullable=False) 


class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(250), nullable=False) 
    height = Column(Float) 
    mass = Column(Float) 
    hair_color = Column(String(250)) 
    eye_color = Column(String(250)) 
    birth_year = Column(String(250)) 
    gender = Column(String(250)) 
    home_world = Column(String(250)) 


class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(250), nullable=False) 
    height = Column(Float) 
    mass = Column(Float) 
    hair_color = Column(String(250)) 
    eye_color = Column(String(250)) 
    birth_year = Column(String(250)) 
    gender = Column(String(250)) 
    home_world = Column(String(250)) 


class CharacterFavorites(Base):
    __tablename__ = 'character_favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    character_id = Column(Integer, ForeignKey('character.id'))
    character = relationship(Character)


class PlanetFavorites(Base):
    __tablename__ = 'Planet_favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship(Planet)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
