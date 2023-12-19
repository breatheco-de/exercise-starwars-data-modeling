import os
import sys
import uuid
from sqlalchemy import Column, ForeignKey, Integer, String, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import ARRAY, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    user = Column(String(250))
    password = Column(String(250))
    created = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    edited = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp(), nullable=False)

class Film(Base):
    __tablename__ = 'film'
    
    id = Column(Integer, primary_key=True)
    characters = Column(String(250))
    director = Column(String(250))
    created = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    edited = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp(), nullable=False)
    episode_id = Column(Integer)
    opening_crawl = Column(String(250))
    producer = Column(String(250))
    release_date = Column(String(250))
    title = Column(String(250))
    url = Column(String(250))

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table character
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    birth_year = Column(String(250))
    eye_color = Column(String(250))
    gender = Column(String(250))
    hair_color = Column(String(250))
    height = Column(Integer)
    homeworld = Column(String(250))
    mass = Column(Integer)
    skin_color = Column(String(250))
    created = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    edited = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp(), nullable=False)
    films = Column(ARRAY(String(250)))
    species = Column(ARRAY(String(250)))
    url = Column(String(250))

class Specie(Base):
    __tablename__ = 'specie'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    average_height = Column(Numeric)
    average_lifespan = Column(Integer)
    classification = Column(String(250))
    designation = Column(String(250))
    created = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    edited = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp(), nullable=False)
    eye_colors = Column(String(250))
    hair_colors = Column(String(250))
    homeworld = Column(String(250))
    language = Column(String(250))
    name = Column(String(250))
    films = Column(ARRAY(String(250)))
    people = Column(ARRAY(String(250)))
    skin_colors = Column(String(250))
    url = Column(String(250))

class Planet(Base):
    __tablename__ = 'planet'

    id = Column(Integer, primary_key=True)
    climate = Column(String(250))
    diameter = Column(Numeric)
    gravity = Column(Numeric)
    created = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    edited = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp(), nullable=False)
    name = Column(String(250))
    orbital_period = Column(Integer)
    population = Column(Integer)
    residents = Column(ARRAY(String(250)))
    rotation_period = Column(Integer)
    surface_water = Column(Integer)
    terrain = Column(String(250))
    url = Column(String(250))

class FavoritePlanet(Base):
    __tablename__ = 'favorite_planet'
    
    id = Column(Integer, primary_key=True)
    user = relationship(User)
    planet = relationship(Planet)
    created = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    edited = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp(), nullable=False)

class FavoriteCharacter(Base):
    __tablename__ = 'favorite_character'
    
    id = Column(Integer, primary_key=True)
    user = relationship(User)
    character = relationship(Character)
    created = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    edited = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp(), nullable=False)
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
