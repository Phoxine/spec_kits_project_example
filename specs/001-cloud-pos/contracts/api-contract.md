# API Contract: Cloud POS Web Application

## Overview
This contract covers the REST API surface for the POS POC backend. The frontend will interact with these endpoints to display products, submit checkout orders, and view order history.

## Endpoints

### GET /products
Returns a paginated product list.

Request
- Query parameters:
  - `search` (optional): string filter for product name or SKU
  - `limit` (optional): integer page size
  - `offset` (optional): integer offset

Response (200)
```json
{
  "items": [
    {
      "id": "string",
      "name": "string",
      "price_cents": 1000,
      "stock": 5
    }
  ],
  "total": 1,
  "limit": 25,
  "offset": 0
}
```

### GET /orders
Returns a list of completed orders.

Request
- Query parameters:
  - `limit` (optional): integer page size
  - `offset` (optional): integer offset

Response (200)
```json
{
  "items": [
    {
      "id": "string",
      "total_amount_cents": 2500,
      "created_at": "2026-05-05T12:00:00Z",
      "status": "confirmed"
    }
  ],
  "total": 1,
  "limit": 25,
  "offset": 0
}
```

### GET /orders/{order_id}
Returns details for a single order.

Response (200)
```json
{
  "id": "string",
  "total_amount_cents": 2500,
  "created_at": "2026-05-05T12:00:00Z",
  "status": "confirmed",
  "items": [
    {
      "product_id": "string",
      "quantity": 2,
      "unit_price_cents": 1200,
      "total_price_cents": 2400
    }
  ]
}
```

### POST /checkout
Submits a cash-only order and confirms inventory deduction.

Request
```json
{
  "items": [
    { "product_id": "string", "quantity": 2 }
  ]
}
```

Response (201)
```json
{
  "order_id": "string",
  "total_amount_cents": 2500,
  "created_at": "2026-05-05T12:00:00Z",
  "status": "confirmed"
}
```

Error Responses
- 400 Bad Request: invalid payload, missing fields
- 409 Conflict: insufficient stock for one or more products
- 500 Internal Server Error: unexpected backend failure

## Notes
- The checkout payload is intentionally minimal for the POC
- Payment method is implicit as `cash` in this phase
- Frontend may use `/products` for both product listing and search
- Order history is scoped to the orders returned by `/orders`
