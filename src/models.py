import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)







class Person (Base):
    __tablename__ = 'Person'
    id = Column (Integer, primary_key=True)
    name =  Column (String(250), nullable=False)
    height = Column(Float , nullable=False)
    mass = Column (Float , nullable=False)
    hair_color = Column (String(250) , nullable=False)
    skin_color = Column (String(250) , nullable=False)
class Planet(Base):
    __tablename__ = 'Planet'
    id = Column (Integer, primary_key=True)
    name =  Column (String(250), nullable=False)
    population = Column(Integer , nullable=False)
    terrain = Column (String(250), nullable=False)
    climate = Column (String(250), nullable=False)
class Starship(Base):
    __tablename__ = 'Starship'
    id = Column (Integer, primary_key=True)
    name =  Column (String(250), nullable=False)
    model = Column (String(250), nullable=False)
    manufacturer = Column (String(250), nullable=False)
    cargo_capacity = Column (Integer, nullable=False) 








# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
