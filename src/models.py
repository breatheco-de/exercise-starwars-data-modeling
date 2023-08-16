import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    climate = Column(String(100))
    terrain = Column(String(100))
    population = Column(Integer)
    # Add more attributes as needed
    residents = relationship('Character', secondary='planet_residents')

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    birth_year = Column(String(20))
    gender = Column(String(20))
    homeworld_id = Column(Integer, ForeignKey('planet.id'))
    homeworld = relationship('Planet', back_populates='residents')
    starships = relationship('Starship', secondary='character_starships')
    vehicles = relationship('Vehicle', secondary='character_vehicles')

class Starship(Base):
    __tablename__ = 'starship'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    model = Column(String(100))
    starship_class = Column(String(100))
    pilots = relationship('Character', secondary='starship_pilots')

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    model = Column(String(100))
    vehicle_class = Column(String(100))
    pilots = relationship('Character', secondary='vehicle_pilots')

class PlanetResidents(Base):
    __tablename__ = 'planet_residents'
    planet_id = Column(Integer, ForeignKey('planet.id'), primary_key=True)
    character_id = Column(Integer, ForeignKey('character.id'), primary_key=True)

class CharacterStarships(Base):
    __tablename__ = 'character_starships'
    character_id = Column(Integer, ForeignKey('character.id'), primary_key=True)
    starship_id = Column(Integer, ForeignKey('starship.id'), primary_key=True)

class CharacterVehicles(Base):
    __tablename__ = 'character_vehicles'
    character_id = Column(Integer, ForeignKey('character.id'), primary_key=True)
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'), primary_key=True)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
