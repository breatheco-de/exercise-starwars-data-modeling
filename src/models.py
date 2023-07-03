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
    name = Column(String(250), nullable=False)
    population = Column(String(10), nullable=False)

class Characters(Base):
    __tablename__ = 'Characters'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gender = Column(String(50), nullable=False)
    hair_color = Column(String(50), nullable=False)
    eye_color = Column(String(50), nullable=False)
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
