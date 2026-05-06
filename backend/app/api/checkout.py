from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import and_
from app.db import SessionLocal
from app.models.product import Product
from app.models.order import Order, OrderStatus
from app.models.order_item import OrderItem
from app.schemas.checkout import CheckoutRequest, CheckoutResponse
from app.auth import require_cashier_or_admin
from datetime import datetime

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=CheckoutResponse, dependencies=[Depends(require_cashier_or_admin)])
def checkout(checkout: CheckoutRequest, db: Session = Depends(get_db)):
    # Start transaction
    total = 0
    order_items = []
    
    # Check inventory and calculate total
    for item in checkout.items:
        product = db.query(Product).filter(Product.id == item.product_id).first()
        if not product:
            raise HTTPException(status_code=400, detail=f"Product {item.product_id} not found")
        if product.stock < item.quantity:
            raise HTTPException(status_code=409, detail=f"Insufficient stock for product {item.product_id}")
        
        unit_price = product.price_cents
        item_total = unit_price * item.quantity
        total += item_total
        
        order_items.append({
            "product_id": item.product_id,
            "quantity": item.quantity,
            "unit_price_cents": unit_price,
            "total_price_cents": item_total
        })
    
    # Deduct stock
    for item in checkout.items:
        product = db.query(Product).filter(Product.id == item.product_id).first()
        product.stock -= item.quantity
    
    # Create order
    order = Order(total_amount_cents=total, status=OrderStatus.confirmed)
    db.add(order)
    db.flush()  # Get order.id
    
    # Create order items
    for item_data in order_items:
        order_item = OrderItem(order_id=order.id, **item_data)
        db.add(order_item)
    
    db.commit()
    
    return CheckoutResponse(
        order_id=order.id,
        total_amount_cents=total,
        created_at=order.created_at.isoformat(),
        status=order.status.value
    )