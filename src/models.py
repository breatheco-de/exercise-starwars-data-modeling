import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

    

class Planetas(Base):
    __tablename__ = 'planetas'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    population = Column(String(250), nullable=False)
    diameter = Column(String(250), nullable=False)
    rotation_period = Column(String(250), nullable=False)
    orbital_period = Column(String(250), nullable=False)
    gravity = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    surface_water = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)


class Characters(Base):
    __tablename__ = 'chraracters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    birth_year = Column(String(250), nullable=False)
    nameye_colore = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)
    hair_color = Column(String(250), nullable=False)
    mass = Column(String(250), nullable=False)


class Fav_Planetas(Base):
    __tablename__ = 'fav_planetas'
    id = Column(Integer, primary_key=True)
    usario_id = Column(Integer, ForeignKey('usuario.id'),
        nullable=False)
    planeta_id = Column(Integer, ForeignKey('planeta.id'),
        nullable=False)

class Fav_Characters(Base):
    __tablename__ = 'fav_characters'
    id = Column(Integer, primary_key=True)
    usario_id = Column(Integer, ForeignKey('usuario.id'),
        nullable=False)
    character_id = Column(Integer, ForeignKey('character.id'),
        nullable=False)

def to_dict(self):
        return {}
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')