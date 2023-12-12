import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()



class User(Base):
    __tablename__ = "User"
    id = Column(Integer, primary_key=True)
    name =  Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    
    character_fav = relationship("Character_fav", back_populates="user")
    planet_fav = relationship("Planet_fav", back_populates="user")
    starship_fav = relationship("Starship_fav", back_populates="user")





class Character(Base):
    __tablename__ = "Character"
    id = Column(Integer, primary_key=True)
    name =  Column(String(250), nullable=False)
    height = Column(Float, nullable=False)
    mass = Column(Float, nullable=False)
    hair_color = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)

    character_fav = relationship("Character_fav", back_populates="character")

class Character_fav(Base):
    __tablename__ = "Character_fav"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("User.id"))
    character_id = Column(Integer, ForeignKey("Character.id"))

    user = relationship("User", back_populates="character_fav")
    character = relationship("Character", back_populates="character_fav")





class Planet(Base):
    __tablename__ = "Planet"
    id = Column(Integer, primary_key=True)
    name =  Column(String(250), nullable=False)
    population = Column(Integer, nullable=False)
    terrain = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)   

    planet_fav = relationship("Planet_fav", back_populates="planet")

class Planet_fav(Base):
    __tablename__ = "Planet_fav"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("User.id"))
    planet_id = Column(Integer, ForeignKey("Planet.id"))

    user = relationship("User", back_populates="planet_fav")
    planet = relationship("Planet", back_populates="planet_fav")





class Starship(Base):
    __tablename__ = "Starship"
    id = Column(Integer, primary_key=True)
    name =  Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    manufacturer = Column(String(250), nullable=False)
    cargo_capacity = Column(Integer, nullable=False)     

    starship_fav = relationship("Starship_fav", back_populates="starship")
    
class Starship_fav(Base):
    __tablename__ = "Starship_fav"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("User.id"))
    starship_id = Column(Integer, ForeignKey("Starship.id"))

    user = relationship("User", back_populates="starship_fav")
    starship = relationship("Starship", back_populates="starship_fav")





render_er(Base, "diagram.png")
