import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)


class Planeta(Base):
    __tablename__ = 'planetas'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    descripcion = Column(String(250))


class Personaje(Base):
    __tablename__ = 'personajes'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    especie = Column(String(250))


class Favoritos(Base):
    __tablename__ = 'favoritos'
    id = Column(Integer, primary_key=True)
    planeta_id = Column(Integer, ForeignKey('planetas.id'))
    personaje_id = Column(Integer, ForeignKey('personajes.id'))

    # Definición de las relaciones con otras tablas
    usuario = relationship(Usuario, backref='favoritos') # Relación uno a muchos con la tabla Usuario
    planeta = relationship(Planeta) # Relación muchos a uno con la tabla Planeta
    personaje = relationship(Personaje) # Relación muchos a uno con la tabla Personaje


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base. Genera el diagrama UML a partir del modelo de datos

render_er(Base, 'diagram.png')
