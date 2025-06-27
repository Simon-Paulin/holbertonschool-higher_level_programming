#!/usr/bin/python3
"""
intro to alchimy class state
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, nullable=True, primary_key=True)
    name = Column(String(128), nullable=False)
