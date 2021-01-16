from fastapi import APIRouter, status
from schemas import Book
import db

book_router = APIRouter(prefix='/books')

@book_router.get('/', status_code=status.HTTP_200_OK)
def get_all_books():
    return db.get_all_books()

@book_router.post('/', status_code=status.HTTP_201_CREATED)
def add_new_book(book: Book):
    response_object = {'status': 'success'}
    try:
        db.add_book_to_db(book)
    except:
        response_object['status'] = 'error'
    return response_object

@book_router.put('/{id}')
def update_book(id: int, book: Book):
    return db.update_book(id, Book)


__all__ = book_router
