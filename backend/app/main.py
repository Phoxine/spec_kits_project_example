from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db import engine, Base
from app.api import products, orders, checkout

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Cloud POS API")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(products.router, prefix="/products", tags=["products"])
app.include_router(orders.router, prefix="/orders", tags=["orders"])
app.include_router(checkout.router, prefix="/checkout", tags=["checkout"])

@app.get("/")
def read_root():
    return {"message": "Cloud POS API"}