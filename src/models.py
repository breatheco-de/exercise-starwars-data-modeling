import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Citizen(Base):
    __tablename__ = 'person'
    chaincode = Column(Integer, primary_key=True, unique=True)
    name = Column(String(250), nullable=False)
    age = Column(Integer, nullable=False)
    species = Column(String(100), nullable=False)
    planet_of_origin = Column(Integer, ForeignKey('planet.id'), nullable=True)
    occupation = Column(String(150), nullable=True)
    date_of_birth = Column(Date, nullable=True)
    gender = Column(String(50), nullable=True)
    status = Column(String(100), nullable=True)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    population = Column(Integer, nullable=True)  # Población total del planeta
    climate = Column(String(100), nullable=True)  # Tipo de clima (árido, templado, frío, etc.)
    terrain = Column(String(100), nullable=True)  # Tipo de terreno (desierto, selva, montaña, etc.)
    gravity = Column(String(50), nullable=True)  # Nivel de gravedad (ejemplos: estándar, alta, baja)
    orbital_period = Column(Integer, nullable=True)  # Tiempo en días para completar una órbita
    rotation_period = Column(Integer, nullable=True)  # Tiempo en horas para completar una rotación
    primary_language = Column(String(100), nullable=True)  # Idioma principal
    description = Column(String(500), nullable=True)  # Descripción del planeta

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
