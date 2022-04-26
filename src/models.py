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
    id = Column(Integer, primary_key = True)
    name = Column(String(250))
    username = Column(String(200), unique=True)
    password = Column(String(200))
    state = Column(String(200))
    favorite_relation = relationship("favorite", back_populates="user")


class Favorite(Base):
    __tablename__="favorite"
    user_id = Column(Integer, ForeignKey("user.id"))
    character_id = Column(Integer, ForeignKey("character.id"))
    planet_id = Column(Integer, ForeignKey("planet.id"))
    vehicle_id = Column(Integer, ForeignKey("vehicle.id"))
    character_name = Column(String(100), ForeignKey('character.id'), primary_key=True)
    planet_name = Column(String(50), ForeignKey('planet.id'), primary_key=True)
    vehicle_name = Column(String(50), ForeignKey('vehicle.id'), primary_key=True)
    user_relation = relationship("user", back_populates="favorite")
    character_relation = relationship("character")
    planet_relation = relationship("planet")
    vehicle_relation = relationship("vehicle")

class character(Base):
    __tablename__ = "character"
    id = Column(Integer, primary_key = True)
    name = Column(String(30), nullable = False, unique = True)
    eyed_color = Column(String(30), nullable = False)
    birth_year = Column(String(30), nullable = False)
    gender = Column(String(30), nullable = False)
    favorite_relation = relationship("favorite")


class planet(Base):
    __tablename__= "planet"
    id = Column(Integer, primary_key = True)
    name = Column(String(30), nullable = False, unique = True)
    rotated_period = Column(Integer)
    diameter = Column(Integer)
    climate = Column(Integer)
    favorite_relation = relationship("favorite")

class vehicle(Base):
    __tablename__= "vehicle"
    id = Column(Integer, primary_key = True)
    name = Column(String(30), nullable = False, unique = True)
    model = Column(String(30), nullable = False)
    favorite_relation = relationship("favorite")


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')