from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from eralchemy2 import render_er
from enum import Enum as PyEnum

Base = declarative_base()

class FavoriteType(PyEnum):
    PLANET = "planet"
    CHARACTER = "character"
    VEHICLE = "vehicle"

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), unique=True, nullable=False)
    email = Column(String(250), unique=True, nullable=False)
    password = Column(String(250), nullable=False)
    
    favorites = relationship('Favorite', back_populates='user')

class Planet(Base):
    __tablename__ = 'Planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(250))
    terrain = Column(String(250))
    population = Column(Integer)
    
    favorites = relationship('Favorite', back_populates='planet')

class Character(Base):
    __tablename__ = 'Character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    species = Column(String(250))
    homeworld = Column(String(250))
    
    favorites = relationship('Favorite', back_populates='character')

class Vehicle(Base):
    __tablename__ = 'Vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250))
    hp = Column(Integer)
    
    favorites = relationship('Favorite', back_populates='vehicle')

class Favorite(Base):
    __tablename__ = 'Favorite'
    user_id = Column(Integer, ForeignKey('User.id'), primary_key=True)
    item_id = Column(Integer, primary_key=True)
    item_type = Column(Enum(FavoriteType), nullable=False)

    user = relationship('User', back_populates='favorites')
    planet_id = Column(Integer, ForeignKey('Planet.id'))
    planet = relationship('Planet', back_populates='favorites')
    
    character_id = Column(Integer, ForeignKey('Character.id'))
    character = relationship('Character', back_populates='favorites')
    
    vehicle_id = Column(Integer, ForeignKey('Vehicle.id'))
    vehicle = relationship('Vehicle', back_populates='favorites')

try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem generating the diagram")
    raise 