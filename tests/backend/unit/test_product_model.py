import pytest
from app.models.product import Product
from app.db import Base

def test_product_creation():
    # Test that Product model can be instantiated
    product = Product(name="Test Product", price_cents=100, stock=10)
    assert product.name == "Test Product"
    assert product.price_cents == 100
    assert product.stock == 10