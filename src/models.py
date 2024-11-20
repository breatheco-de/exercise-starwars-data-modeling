import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Planet(db.Model):
    __tablename__ = 'planet'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    popilation = db.Column(db.integer)
    wather = db.Column(db.String(50), nullable=False)




    def __rep__(self):
        return {Planet %r} % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,


        }

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
