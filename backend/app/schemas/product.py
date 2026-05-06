from pydantic import BaseModel, Field
from typing import Optional

class ProductBase(BaseModel):
    name: str
    price_cents: int = Field(..., ge=0)
    stock: int = Field(..., ge=0)

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class Product(ProductBase):
    id: int
    created_at: str
    updated_at: Optional[str]

    class Config:
        from_attributes = True