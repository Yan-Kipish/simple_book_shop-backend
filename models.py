from sqlalchemy import Column, Integer, String, Float, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String(length=32), nullable=False, unique=True)
    author = Column(String(length=96), nullable=False)
    price = Column(Float, nullable=False)
    description = Column(Text, default="")


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String(length=96), nullable=False)
    email = Column(String(length=96), nullable=False)
    password = Column(String(length=96), nullable=False)

    isAdmin = Column(Boolean)
