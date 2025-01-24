import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    pasword = Column(String(120), nullable=False)
    first_name = Column(String(80), nullable=False)
    last_name = Column(String(80), nullable=False)
    subscription_date = Column(DateTime, default=datetime.utcnow)

    favorites = relationship('Favorite', back_populates='user')

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True, nullable=False)
    climate = Column(String(120))
    terrain = Column(String(120))
    population = Column(Integer)

    favorites = relationship('Favorite', back_populates='planet')

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True, nullable=False)
    gender = Column(String(10))
    birth_year = Column(String(20))
    eye_color = Column(String(20))

    favorites = relationship('Favorite', back_populates='character')

class Ship(Base):
    __tablename__ = 'ship'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True, nullable=False)
    model = Column(String(120))
    manufacturer = Column(String(120))
    crew = Column(Integer)
    passengers = Column(Integer)

    favorites = relationship('Favorite', back_populates='ship')

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=True)
    character_id = Column(Integer, ForeignKey('character.id'), nullable=True)
    ship_id = Column(Integer, ForeignKey('ship.id'), nullable=True)

    user = relationship('User', back_populates='favorites')
    planet = relationship('Planet', back_populates='favorites')
    character = relationship('Character', back_populates='favorites')
    ship = relationship('Ship', back_populates='favorites')

## Draw from SQLAlchemy base
try:
    render_er(Base, 'diagram.png')
    print("¡Diagrama UML generado correctamente")
except Exception as e:
    print("Error al generar el diagrama UML:", e)
