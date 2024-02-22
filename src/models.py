import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er


Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(16), nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(50))


class Posts(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    description = Column(String(500))
    body = Column(String(2000), nullable=False)
    img_url = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    users = relationship('Users')

    def to_dict(self):
        return {}


class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    homeworld_id = Column(Integer, ForeignKey('planets.id'))
    homeworld = relationship('Planets')


class Films(Base):
    __tablename__ = 'films'
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    director = Column(String(150), nullable=False)
    year = Column(DateTime)


class CharactersFilms(Base):
    __tablename__ = 'characters_films'
    id = Column(Integer, primary_key=True)
    minutes = Column(DateTime)
    character_id = Column(Integer, ForeignKey('characters.id'))
    film_id = Column(Integer, ForeignKey('films.id'))
    character = relationship('Characters', foreign_keys=['character_id'])  # falta el parametro del foreingkey
    film = relationship('Films', foreign_keys=['film_id'])  # falta el parametro del foreingkey


class FavoritePlanet(Base):
    __tablename__ = 'favorite_planet'
    
    id = Column(Integer, primary_key=True)
    planet_id = Column(Integer, ForeignKey('planets.id'))
    planet = relationship('Planets')
    

class FavoriteCharacter(Base):
    __tablename__ = 'favorite_character'
    
    id = Column(Integer, primary_key=True)
    characters_id = Column(Integer, ForeignKey('characters.id'))
    characters = relationship('Characters')
    

# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')