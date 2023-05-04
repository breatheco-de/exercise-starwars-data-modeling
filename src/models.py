import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class MyUser(Base):
    __tablename__ = 'my_user'
 
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(250), nullable=False)
    favorite = relationship('favorite')

class Location(Base):
    __tablename__ = 'location'
 
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False, unique=True)
    type = Column(String(250), nullable=False)
    dimension = Column(String(250), nullable=False)
    favorite = relationship('favorite')

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False, unique=True)
    status = Column(String(250), nullable=False)
    species = Column(String(250), nullable=False)
    favorite = relationship('favorite')

class Episode(Base):
    __tablename__ = 'episode'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False, unique=True)
    status = Column(String(250), nullable=False)
    favorite = relationship('favorite')

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('my_user.id'))
    location_id = Column(Integer, ForeignKey('location.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    episode_id = Column(Integer, ForeignKey('episode.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
