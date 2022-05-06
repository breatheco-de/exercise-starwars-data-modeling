import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er


Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    favorites = relationship('favorite', backref='user', uselist=True)
    email = Column(String(50), unique=True, nullable=False)
    username = Column(String(30), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class Favorite(Base):
    __tablename__ = "favorite"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    # user = relationship('user')
    character_id = Column(Integer, ForeignKey('character.id'), nullable=False)
    # character = relationship('character')
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=False)
    # planet = relationship('character)


class Character(Base):
    __tablename__ = "character"
    id = Column(Integer, primary_key=True)


class Planet(Base):
    __tablename__ = "planet"
    id = Column(Integer, primary_key=True)


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')