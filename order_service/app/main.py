from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session
from app.models.order_model import Order
from app.deps import get_session
from app.crud.order_crud import create_order, get_order, get_orders

app = FastAPI()

@app.post("/orders/", response_model=Order)
def create_order_endpoint(order: Order, db: Session = Depends(get_session)):
    return create_order(db, order)

@app.get("/orders/{order_id}", response_model=Order)
def get_order_endpoint(order_id: int, db: Session = Depends(get_session)):
    db_order = get_order(db, order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order

@app.get("/orders/", response_model=list[Order])
def get_orders_endpoint(db: Session = Depends(get_session)):
    return get_orders(db)

