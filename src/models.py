import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    surname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)


class Vehicles(Base):
    __tablename__ = 'Vehicles'
    id = Column(Integer, primary_key=True)
    model = Column(String(250), nullable=False)
    vehicle_name = Column(String(250), nullable=False)


class Fave_Vehicles(Base):
    __tablename__ = 'Fave_Vehicles'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("User.id"), nullable=False)
    vehicle_name = Column(Integer, ForeignKey("Vehicles.id"), nullable=False)

class Characters(Base):
    __tablename__ = 'Characters'
    id = Column(Integer, primary_key=True)
    character_name = Column(String(250), nullable=False)

class Fave_chars(Base):
    __tablename__ = 'Fave_chars'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("User.id"), nullable=False)
    character_id = Column(Integer, ForeignKey("Characters.id"), nullable=False)

class Planets(Base):
    __tablename__ = 'Planets'
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey("Characters.id"), nullable=False)

class Fave_plts(Base):
    __tablename__ = 'Fave_plts'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("User.id"), nullable=False)
    planet_id = Column(Integer, ForeignKey("Planets.id"), nullable=False)

try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e