from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import db_models
import valid_models

base_engine = create_engine('sqlite:///simple_book_db.db')
Session = sessionmaker(bind=base_engine)
session = Session()


def add_book_to_db(book: valid_models.Book):
    new_book = db_models.Book(**dict(book))
    session.add(new_book)
    session.commit()

def get_all_books():
    books_db = session.query(db_models.Book).all()
    validate_orm = lambda book: valid_models.Book.from_orm(book)
    books_valid = list(map(validate_orm, books_db))
    return books_valid
    
def get_book_by_title(title_input: str):
    book = session.query(db_models.Book).filter_by(title=title_input).first()
    if not book:
        return None
    return valid_models.Book.from_orm(book)
