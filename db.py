from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

import models
import schemas

base_engine = create_engine('sqlite:///simple_book_db.db')
# Session = sessionmaker(bind=base_engine, autocommit=False)
# session = Session()
session = scoped_session(sessionmaker(bind=base_engine, autocommit=False))

def add_book_to_db(book: schemas.Book):
    new_book = models.Book(**dict(book))
    try:
        session.add(new_book)
        session.commit()
    except:
        session.rollback()
    finally:
        session.close()

def get_all_books():
    try:
        books_db = session.query(models.Book).all()
        validate_orm = lambda book: schemas.Book.from_orm(book)
        books_valid = list(map(validate_orm, books_db))
    except:
        session.rollback()
        books_valid = []
    finally:
        session.close()
    return books_valid
    
def update_book(id: int, book: schemas.Book):
    result = "success"
    try:
        session.query(models.Book).\
            filter(models.Book.id == id).\
            update(**book)
        session.commit()
    except:
        session.rollback()
        result = "error"
    finally:
        session.close()
    
    return {"result": result}

def get_customer(email: str, password: str, *args, **kwargs):
    customer = session.query(models.Customer).filter_by(email=email, password=password).first()
    session.close()
    result = "success" if customer else "error"
    return {"result": result}

def add_user_to_db(customer: schemas.Customer):
    new_customer = models.Customer(**dict(customer))
    try:
        session.add(new_customer)
        session.commit()
    except:
        session.rollback()
    finally:
        session.close()
