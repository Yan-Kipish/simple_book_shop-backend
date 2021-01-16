from fastapi import APIRouter, status
from schemas import Customer
import db

auth_router = APIRouter(prefix='/auth')

@auth_router.post('/')
def login(customer: Customer):
    return db.get_customer(**dict(customer))

@auth_router.post('/register')
def register(customer: Customer):
    db.add_user_to_db()

__all__ = auth_router
