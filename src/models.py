import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

'''class Address(Base):
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
'''
class User(Base):
    __tablename__="user"
    id=Column(Integer, primary_key=True)
    username=Column(String(250), nullable=False)
    password_hash=Column(String(250))

class Character(Base):
    __tablename__="character"
    id=Column(Integer, primary_key=True)
    name=Column(String(250), nullable=False)
    description=Column(String(512), nullable=False)
    imgPath=Column(String(256), nullable=False)


class Planet(Base):
    __tablename__="planet"
    id=Column(Integer, primary_key=True)
    name=Column(String(250), nullable=False)
    description=Column(String(512), nullable=False)
    imgPath=Column(String(256), nullable=False)

class Favorite(Base):
    __tablename__="favorite"
    id=Column(Integer,primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    planet_id = Column(Integer, ForeignKey("planet.id"))
    character_id = Column(Integer, ForeignKey("character.id"))


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')