from typing import Optional
from pydantic import BaseModel, EmailStr

class Book(BaseModel):
    title: str
    author: str
    price: float
    description: Optional[str] = None

    class Config:
        orm_mode = True

class Customer(BaseModel):
    name: str
    email: EmailStr
