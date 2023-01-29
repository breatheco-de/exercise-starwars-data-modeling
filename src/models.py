import os
import sys
import uuid
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import ARRAY, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Film(Base):
    __tablename__ = 'film'
    
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    person = relationship('FilmPerson', uselist=True, backref='film')

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    birth_year = Column(String(250))
    eye_color = Column(String(250))
    films = relationship('FilmPerson', uselist=True, backref='person')
    gender = Column(String(250))
    hair_color = Column(String(250))
    height = Column(Integer)
    homeworld = Column(String(250))
    mass = Column(Integer)
    skin_color = Column(String(250))
    created = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    edited = Column(TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp(), nullable=False)
    species = Column(ARRAY(String(250)))
    starships = Column(ARRAY(String(250)))
    url = Column(String(250))
    starships = Column(ARRAY(String(250)))

class FilmPerson(Base):
    __tablename__ = 'person_movies'

    person_id = Column(UUID(as_uuid=True), ForeignKey('person.id'))
    movie_id = Column(UUID(as_uuid=True), ForeignKey('film.id'))


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
