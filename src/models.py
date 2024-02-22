import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(200), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    name = Column(String(100), nullable=False)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    population = Column(Integer, nullable=False)

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    homeworld= Column(String(50), ForeignKey('planet.name'))
    planet = relationship(Planet)

class Film(Base):
    __tablename__ = 'film'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    director = Column(String(50), nullable=False)
    characters = Column(String(50),ForeignKey('character.name'))
    character = relationship(Character)


class Director(Base):
    __tablename__ = 'director'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    surname = Column(String(100), nullable=False)
    films = Column(String(50),ForeignKey('film.name'))
    film = relationship(Film)
    

class Favorite(Base):
    __tablename__ = 'favorites'
    id = Column(Integer,primary_key=True)
    user_id = Column(Integer,ForeignKey('user.id'))
    user = relationship(User)
    favorite_planets = Column(String(50),ForeignKey('planet.name'))
    planets = relationship(Planet)
    favorite_characters = Column(String(50),ForeignKey('character.name'))
    character = relationship(Character)
    favorite_films = Column(String(50),ForeignKey('film.name'))
    film = relationship(Film)
    favorite_directors = Column(String(50),ForeignKey('director.name'))
    director = relationship(Director)


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
