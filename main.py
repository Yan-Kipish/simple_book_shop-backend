from typing import Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schemas import Book
import db
import routers

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

@app.get('/')
def hello():
    return {"result": "Hello, World!"}

@app.get('/ping')
def ping():
    return {"result": "pong!"}

app.include_router(routers.book_router)
