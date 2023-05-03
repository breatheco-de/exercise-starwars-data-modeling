import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean, func
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
 
Base = declarative_base()
 
 
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(256), unique=True, nullable=False)
    password = Column(String(128), nullable=False)
    created_date = Column(DateTime, default=func.now())
    admin_status = Column(Boolean, default=False)
    

 
class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    rotation_period = Column(Integer, nullable=False)
    orbital_period = Column(Integer, nullable=False)
    diameter = Column(Integer, nullable=False)
    climate = Column(String(128), nullable=False)
    gravity = Column(String(128), nullable=False)
    terrain = Column(String(128), nullable=False)
    population = Column(Integer, nullable=False)
    url_image = Column(String(250), unique=False)


class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    species = Column(String(200), nullable=False)
    height = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    eye_color = Column(Integer, nullable=False)
    birth_year = Column(Integer, nullable=False)
    gender = Column(String(200), nullable=False)
    url_image = Column(String(250), unique=False)
    
 
class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planets.id'))
    people_id = Column(Integer, ForeignKey('people.id'))
 
# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
