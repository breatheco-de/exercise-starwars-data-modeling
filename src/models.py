import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    email  = Column(String(80), nullable=False)


class Posts(Base):
    __tablename__ = 'Posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    body = Column(String(1000))
    user_id = Column(Integer, ForeignKey('User.id'))
    User = relationship(User)

class Comments(Base):
    __tablename__ = 'Comments'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(1000), nullable=False)
    post_id = Column(Integer, ForeignKey("Posts.id"))
    Posts = relationship(Posts)
    user_id = Column(Integer, ForeignKey("User.id"))
    User = relationship(User)

class Follower():
    __tablename__ = 'Follower'
    user_from_id = Column(Integer, ForeignKey("User.id"))
    user_to_id = Column(Integer, ForeignKey("User.id"))
    user_from = relationship(User)
    user_to = relationship(User)


    def to_dict(self):
        return {}


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
