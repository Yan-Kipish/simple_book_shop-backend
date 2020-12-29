from typing import Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import db

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Book(BaseModel):
    title: str
    author: str
    price: float
    description: Optional[str] = None


@app.get('/ping')
def hello():
    return {"result": "pong!"}


@app.get('/books')
def get_books():
    return {
        "status": "success",
        "books": db.BOOKS
    }

@app.post('/books')
def new_books(book: Book):
    response_object = {'status': 'success'}
    db.BOOKS.append(book)
    return response_object
