from fastapi import APIRouter
from valid_models import Book
import db

book_router = APIRouter(prefix='/books')

@book_router.get('/')
def get_books():
    """
    Даний endpoint видає усі книги у базі
    """
    return {
        "status": "success",
        "books": db.get_all_books()
    }

@book_router.post('/')
def new_books(book: Book):
    response_object = {'status': 'success'}
    try:
        db.add_book_to_db(book)
    except:
        response_object['status'] = 'error'
    return response_object

@book_router.get('/{title}')
def get_books_by_id(title: str):
    response_object = {'result': 'success'}
    book = db.get_book_by_title(title)
    response_object['body'] = book
    return response_object

__all__ = book_router
