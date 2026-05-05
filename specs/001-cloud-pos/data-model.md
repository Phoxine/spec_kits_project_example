# Data Model: Cloud POS Web Application

## Entities

### Product
- id: UUID or integer primary key
- name: string
- price_cents: integer (price in cents to avoid floating-point errors)
- stock: integer (current available inventory)
- created_at: timestamp
- updated_at: timestamp

Validation
- `name` is required and non-empty
- `price_cents` must be >= 0
- `stock` must be >= 0

### Order
- id: UUID or integer primary key
- total_amount_cents: integer (final order total)
- created_at: timestamp
- status: string enum (`confirmed`, `refunded`)

Validation
- `total_amount_cents` must be >= 0
- `status` must be one of the allowed values

### OrderItem
- id: UUID or integer primary key
- order_id: foreign key to Order
- product_id: foreign key to Product
- quantity: integer
- unit_price_cents: integer
- total_price_cents: integer

Validation
- `quantity` must be > 0
- `unit_price_cents` must be >= 0
- `total_price_cents` must equal `quantity * unit_price_cents`

## Relationships
- One `Order` has many `OrderItem` records
- Each `OrderItem` references one `Product`
- Inventory is deducted from `Product.stock` when an `Order` is confirmed

## Transaction Rules
- Checkout must execute in a single database transaction
- Product stock is decremented only if all items have sufficient inventory
- Orders are only committed when stock validation passes
- Prevent negative stock by checking product availability before deduction

## Scope Notes
- No customer or user-role entities are included in the POC
- Order history is scoped to the order records created by the checkout flow
