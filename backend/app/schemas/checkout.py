from pydantic import BaseModel
from typing import List

class CheckoutItem(BaseModel):
    product_id: int
    quantity: int

class CheckoutRequest(BaseModel):
    items: List[CheckoutItem]

class CheckoutResponse(BaseModel):
    order_id: int
    total_amount_cents: int
    created_at: str
    status: str