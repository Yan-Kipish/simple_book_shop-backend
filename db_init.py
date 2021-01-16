from db import add_book_to_db, base_engine, add_user_to_db
import schemas
import models

BOOKS = [
    {
        'title': 'Оформляндія або Прогулянка в Зону',
        'author': 'Маркіян Камиш',
        'price': 146.00,
        'description': ""
    },
    {
        'title': 'Культ',
        'author': 'Любко Дереш',
        'price': 280.00,
        "description": "Lorem Ipsum"
    },
    {
        'title': 'Мифы древней Греции',
        'author': 'Эксмо',
        'price': 139.99
    }
]
USERS = [
    {
        'name': 'Yan',
        'email': 'y@x.com',
        'password': 'pwd',
        'isAdmin': True
    },
    {
        'name': 'Lol',
        'email': 'kek322@gmail.com',
        'password': 'q1w2e3r4t5'
    }
]
models.Base.metadata.create_all(base_engine)
for book in BOOKS:
    json_book = schemas.Book(**book)
    add_book_to_db(json_book)

for user in USERS:
    json_user = schemas.Customer(**user)
    add_user_to_db(json_user)
