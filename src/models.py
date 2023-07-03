import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'Users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    surname = Column(String(250), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(20), nullable=False)

class Planets(Base):
    __tablename__ = 'Planets'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
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

class Characters(Base):
    __tablename__ = 'Characters'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    species = Column(String(200), nullable=False)
    height = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    eye_color = Column(Integer, nullable=False)
    birth_year = Column(Integer, nullable=False)
    gender = Column(String(200), nullable=False)
    url_image = Column(String(250), unique=False)
    planet_born_id = Column(Integer, ForeignKey('Planets.id'))

class Favorits(Base):
    __tablename__ = 'Favorits'
    id = Column(Integer, primary_key=True)
    id_Users = Column(Integer, ForeignKey('Users.id'))
    id_Planets = Column(Integer, ForeignKey('Planets.id'))
    id_Characters = Column(Integer, ForeignKey('Characters.id'))

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     usuario_id = Column(Integer, ForeignKey('usuario.id'))
    # Users = relationship(Usuario)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
