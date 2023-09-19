import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    ID = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False, unique=True)
    firstname = Column(String(250), nullable=True)
    lastname = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)

class Planet(Base):
    __tablename__ = 'planet'
    ID = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False, unique=True)
    description = Column(String(500))

class Character(Base):
    __tablename__ = 'character'
    ID = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False, unique=True)
    description = Column(String(500))

user_planet_association = Table('user_planet', Base.metadata,
    Column('user_id', Integer, ForeignKey('user.ID')),
    Column('planet_id', Integer, ForeignKey('planet.ID'))
)

user_character_association = Table('user_character', Base.metadata,
    Column('user_id', Integer, ForeignKey('user.ID')),
    Column('character_id', Integer, ForeignKey('character.ID'))
)

User.favorite_planets = relationship('Planet', secondary=user_planet_association, backref="users")
User.favorite_characters = relationship('Character', secondary=user_character_association, backref="users")

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
