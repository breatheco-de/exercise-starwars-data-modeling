import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id_usuario = Column(Integer, primary_key=True)
    nombre = Column(String(20), nullable=False)
    apellido = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(12), nullable=False)
    fecha_suscripcion = Column(String(12))
    id_personaje = Column(Integer, ForeignKey("personaje.id_personaje"))
    personaje = relationship("Personaje")


class Personaje(Base):
    __tablename__ = 'personaje'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id_personaje= Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)

class Fav_person_plan(Base):
    __tablename__ = 'fav_person_plan'
    id_fav = Column(Integer,primary_key=True)
    id_usuario = Column(Integer, ForeignKey("usuario.id_usuario"))
    id_personaje = Column(Integer, ForeignKey("personaje.id_personaje"))
    id_planeta = Column(Integer, ForeignKey("planeta.id_planeta"))

class Planeta(Base):
    __tablename__ = 'planeta'
    id_planeta = Column(Integer,primary_key=True)
    nombre = Column(String(20), nullable=False)



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
