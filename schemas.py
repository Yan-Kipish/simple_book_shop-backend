from typing import Optional
from pydantic import BaseModel, EmailStr

class Book(BaseModel):
    title: str
    author: str
    price: float
    description: Optional[str]

    class Config:
        orm_mode = True

class Customer(BaseModel):
    name: Optional[str]
    email: EmailStr
    password: str
