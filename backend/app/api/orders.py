from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db import SessionLocal
from app.models.order import Order as OrderModel
from app.models.order_item import OrderItem
from app.schemas.order import Order
from app.auth import require_cashier_or_admin

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[Order], dependencies=[Depends(require_cashier_or_admin)])
def read_orders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    orders = db.query(OrderModel).offset(skip).limit(limit).all()
    # Include items
    for order in orders:
        order.items = db.query(OrderItem).filter(OrderItem.order_id == order.id).all()
    return orders

@router.get("/{order_id}", response_model=Order, dependencies=[Depends(require_cashier_or_admin)])
def read_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(OrderModel).filter(OrderModel.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    order.items = db.query(OrderItem).filter(OrderItem.order_id == order.id).all()
    return order