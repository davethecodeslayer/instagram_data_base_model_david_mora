import os
import sys
from sqlalchemy import (Column, ForeignKey, Integer, String) 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    username = Column (String(15), nullable=False, unique=True)
    password = Column(String(20), nullable=False, unique=True)
    follower = relationship('Follower')
    post = relationship('Post')
    comment = relationship('Comment')

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_to_id = Column(Integer, ForeignKey('user.id'), nullable=True)
    user_from_id = Column(Integer, ForeignKey('user.id'), nullable=True)

class Post(Base): 
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    follower_id = Column(Integer, ForeignKey('user.id'))
    comment = relationship('Comment')
    media = relationship('Media')

class Comment(Base): 
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(300), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))

class Media(Base): 
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    url = Column(String(250), nullable=False)
    


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e