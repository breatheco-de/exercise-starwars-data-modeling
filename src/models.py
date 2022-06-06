import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Base2(Base):
    __abstract__ = True
    #created = Column(DateTime(timezone=True), default=func.now())


class User(Base2):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(80), unique=False, nullable=False)
    planet = Column(String(25), nullable=False)
    favorites = relationship("Favorites", backref="user", uselist=True)


class Favorites(Base2):
    __tablename__ = "favorites"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    items = Column(Integer, ForeignKey("item.id"), nullable=False)
    # character_id = Column(Integer, ForeignKey("character.id"))
    # planet_id = Column(Integer, ForeignKey("planet.id"))


class Item(Base2):
    __tablename__ = "item"
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    type = Column(String(20), nullable=False)
    favorites = relationship("Favorites", backref="item")
    
    __mapper_args__ = {"polymorphic_identity": "item", "polymorphic_on": type}


class Character(Item):
    __tablename__ = "character"
    id = Column(Integer, ForeignKey("item.id"), primary_key=True)
    uid = Column(Integer)
    height = Column(String(150))
    gender = Column(String(150))
    mass = Column(String(150))
    birth_year = Column(String(150))
    skin_color = Column(String(150))
    # favorites = relationship("Favorites", backref="character", uselist=True)

    __mapper_args__ = {"polymorphic_identity": "characters"}
   

class Planet(Item):
    __tablename__ = "planet"
    id = Column(Integer, ForeignKey("item.id"), primary_key=True)
    uid = Column(Integer)
    population = Column(String(150))
    terrain = Column(String(150))
    diameter = Column(String(150))
    climate = Column(String(150))
    gravity = Column(String(150))
    # favorites = relationship("Favorites", backref="planet", uselist=True)

    __mapper_args__ = {"polymorphic_identity": "planets"}

    
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')