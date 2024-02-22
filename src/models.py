import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    email = Column(String(200), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)

class Planet(Base):
    __tablename__ = 'planets'
    planet_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    population = Column(Integer, nullable=False)

class Character(Base):
    __tablename__ = 'characters'
    character_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    homeworld= Column(String(50), ForeignKey('planets.name'))
    planet = relationship(Planet)

class Director(Base):
    __tablename__ = 'directors'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)

class Film(Base):
    __tablename__ = 'films'
    film_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    director_name = Column(String(50),ForeignKey('directors.first_name'))
    director = relationship(Director)

class CharacterFilm(Base):
    __tablename__ = 'character_films'
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer,ForeignKey('characters.character_id'))
    film_id = Column(Integer,ForeignKey('films.film_id'))
    minutes = Column(Integer,nullable=True)
    characters = relationship(Character)
    films = relationship(Film)

class FavoriteCharacters(Base):
    __tablename__ = 'favorite_characters'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer,ForeignKey('users.user_id'))
    character_id = Column(Integer,ForeignKey('characters.character_id'))
    characters = relationship(Character)
    users = relationship(User)

class FavoriteFilms(Base):
    __tablename__ = 'favorite_films'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer,ForeignKey('users.user_id'))
    film_id = Column(Integer,ForeignKey('films.film_id'))
    users = relationship(User)
    films = relationship(Film)

class FavoritePlanets(Base):
    __tablename__ = 'favorite_planets'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer,ForeignKey('users.user_id'))
    planet_id = Column(Integer,ForeignKey('planets.planet_id'))
    users = relationship(User)
    planets = relationship(Planet)


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
