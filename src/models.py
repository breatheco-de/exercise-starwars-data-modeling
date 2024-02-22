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
    username= Column(String(50),nullable=False)
    password = Column(String(50), nullable=False)
    name = Column(String(100), nullable=False)
    surname = Column(String(100), nullable=False)
    email = Column(String(200), nullable=False)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(1000), nullable=False)

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(1000), nullable=False)

class Favorite(Base):
    __tablename__ = 'favorites'
    id = Column(Integer,primary_key=True)
    user_id = Column(Integer,ForeignKey('user.id'))
    username = Column(String(50),nullable=False)
    user = relationship(User)
    planet_id = Column(Integer,ForeignKey('planet.id'))
    planet_name = Column(String(100), nullable=False)
    planet = relationship(Planet)
    char_id = Column(Integer,ForeignKey('character.id'))
    char = Column(String(100), nullable=False)
    planet = relationship(Character)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
