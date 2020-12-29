from db import add_book_to_db, base_engine
import valid_models
import db_models

BOOKS = [
    {
        'title': 'Оформляндія або Прогулянка в Зону',
        'author': 'Маркіян Камиш',
        'price': 146.00
    },
    {
        'title': 'Культ',
        'author': 'Любко Дереш',
        'price': 280.00
    },
    {
        'title': 'Мифы древней Греции',
        'author': 'Эксмо',
        'price': 139.99
    }
]

db_models.Base.metadata.create_all(base_engine)
for book in BOOKS:
    json_book = valid_models.Book(**book)
    add_book_to_db(json_book)
