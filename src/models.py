from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), unique=True, nullable=False)
    email = Column(String(250), unique=True, nullable=False)
    password = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    
    favorite_characters = relationship('FavoriteCharacter', back_populates='user')
    favorite_planets = relationship('FavoritePlanet', back_populates='user')
    favorite_vehicles = relationship('FavoriteVehicle', back_populates='user')

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(250))
    terrain = Column(String(250))
    population = Column(Integer)
    
class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    species = Column(String(250))
    homeworld = Column(String(250))
    
    favorite_characters = relationship('FavoriteCharacter', back_populates='character')

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250))
    hp = Column(Integer)

class FavoriteCharacter(Base):
    __tablename__ = 'favorite_character'
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    character_id = Column(Integer, ForeignKey('character.id'), primary_key=True)

    user = relationship('User', back_populates='favorite_characters')
    character = relationship('Character', back_populates='favorite_characters')

class FavoritePlanet(Base):
    __tablename__ = 'favorite_planet'
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    planet_id = Column(Integer, ForeignKey('planet.id'), primary_key=True)

    user = relationship('User', back_populates='favorite_planets')
    planet = relationship('Planet', back_populates='favorite_planets')

class FavoriteVehicle(Base):
    __tablename__ = 'favorite_vehicle'
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'), primary_key=True)

    user = relationship('User', back_populates='favorite_vehicles')
    vehicle = relationship('Vehicle', back_populates='favorite_vehicles')