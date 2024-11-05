import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from datetime import datetime, timezone

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(40), nullable=False, unique=True)
    password = Column(String(40), nullable=False)
    full_name = Column(String(200), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    created = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    
    favorites = relationship('Favorite', backref='user', lazy=True)

class Planet(Base):
    __tablename__ = 'planet'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    diameter = Column(String(100), nullable=False)
    rotation_period = Column(String(100), nullable=False)
    orbital_period = Column(String(100), nullable=False)
    gravity = Column(String(100), nullable=False)
    population = Column(String(100), nullable=False)
    climate = Column(String(100), nullable=False)
    terrain = Column(String(100), nullable=False)
    surface_water = Column(String(100), nullable=False)
    created = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    edited = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    
    favorites = relationship('Favorite', backref='planet', lazy=True)

class Vehicle(Base):
    __tablename__ = 'vehicle'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    model = Column(String(100), nullable=False)
    vehicle_class = Column(String(100), nullable=False)
    manufacturer = Column(String(100), nullable=False)
    length = Column(String(100), nullable=False)
    cost_in_credits = Column(String(100), nullable=False)
    crew = Column(String(100), nullable=False)
    max_atmosphering_speed = Column(String(100), nullable=False)
    cargo_capacity = Column(String(100), nullable=False)
    consumables = Column(String(100), nullable=False)
    url = Column(String(200), nullable=False)
    created = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    edited = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    
    favorites = relationship('Favorite', backref='vehicle', lazy=True)

class People(Base):
    __tablename__ = 'people'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    birth_year = Column(String(100), nullable=False)
    eye_color = Column(String(100), nullable=False)
    gender = Column(String(100), nullable=False)
    hair_color = Column(String(100), nullable=False)
    height = Column(String(20), nullable=False)
    mass = Column(String(40), nullable=False)
    skin_color = Column(String(20), nullable=False)
    homeworld = Column(String(40), nullable=False)
    url = Column(String(100), nullable=False)
    created = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    edited = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    
    favorites = relationship('Favorite', backref='people', lazy=True)

class Favorite(Base):
    __tablename__ = 'favorite'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    people_id = Column(Integer, ForeignKey('people.id'), nullable=True)
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'), nullable=True)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=True)

# Generate a diagram for the database schema
render_er(Base, 'diagram.png')
