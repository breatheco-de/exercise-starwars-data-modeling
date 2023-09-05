import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class item(Base):
    __abstract__ = True
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)
    url= Column(String(256), nullable=False)
    

class Character(item):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    birth_year = Column(String(256))
    eye_color = Column(String(256))
    gender = Column(String(256))
    height = Column(Integer)
    mass = Column(Integer)
    starship = Column(String(256))
    vehicles = Column(String(256))
    children1=relationship("Favorite",back_populates="parent1")

    

class Planet(item):
    __tablename__= 'planet'
    diameter=Column(String(256))
    rotation_period=Column(String(256))
    orbital_period=Column(String(256))
    gravity=Column(String(256))
    population=Column(Integer)
    climate=Column(String(256))
    residents=Column(String(256))
    terrain=Column(String(256))
    children2=relationship("Favorite",back_populates="parent2")

class Vehicle(item):
    __tablename__='vehicle'
    vehicle_class=Column(String(256))
    manufacturer=Column(String(256))
    length=Column(Integer)
    cost_in_credits=Column(Integer)
    crew=Column(String(256))
    passengers=Column(Integer)
    cargo_capacity=Column(Integer)
    consumable=Column(String(256))
    children3=relationship("Favorite",back_populates="parent3")

class Favorite(Base):
    __tablename__='favorite'
    id=Column(Integer,primary_key=True)
    id_user=Column(Integer,ForeignKey('user.id_user'))
    character_fav=Column(Integer,ForeignKey('character.id'))
    planet_fav=Column(Integer,ForeignKey('planet.id'))
    vehicle_fav=Column(Integer,ForeignKey('vehicle.id'))
    parent1=relationship("Character",back_populates="children1")
    parent2=relationship("Character",back_populates="children2")
    parent3=relationship("Character",back_populates="children3")

class User(Base):
    __tablename__='user'
    id_user=Column(Integer, primary_key=True)
    password=Column(String(256))

    def to_dict(self):
        return {}



render_er(Base, 'diagram.png')
