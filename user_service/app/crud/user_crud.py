# app/crud/user_crud.py
from sqlmodel import Session, select
from app.models.user_model import User
from app.db_engine import engine

def get_user(user_id: int):
    with Session(engine) as session:
        user = session.get(User, user_id)
        return user

def create_user(user: User):
    with Session(engine) as session:
        session.add(user)
        session.commit()
        session.refresh(user)
        return user
