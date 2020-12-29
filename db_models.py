from sqlalchemy import Column, Integer, String, Float, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Book(Base):
    """
    Модель книги.
    id - первинний ключ, унікальний ідентифікатор книги у БД
    title - назва книги, обов'язкове поле
    author - автор книги, обов'язкове поле
    price - ціна за штуку, обов'язкове поле
    description - короткий опис книги
    """
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String(length=32), nullable=False, unique=True)
    author = Column(String(length=96), nullable=False)
    price = Column(Float, nullable=False)
    description = Column(Text)

