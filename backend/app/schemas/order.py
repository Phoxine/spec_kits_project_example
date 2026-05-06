from pydantic import BaseModel
from typing import List, Optional

class OrderItemBase(BaseModel):
    product_id: int
    quantity: int
    unit_price_cents: int
    total_price_cents: int

class OrderBase(BaseModel):
    total_amount_cents: int
    status: str

class Order(OrderBase):
    id: int
    created_at: str
    items: List[OrderItemBase]

    class Config:
        from_attributes = True