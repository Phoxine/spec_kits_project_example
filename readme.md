

Get Started

```
uvx --from git+https://github.com/github/spec-kit.git specify init --here
```

Establish project principles

```
/speckit.constitution

Create principles focused on code quality, testing standards, user experience consistency, and performance requirements. As a mininum viable product, do not over design.
```

Create the spec

```
/speckit.specify

Build a cloud-based POS web application for small retail businesses.

Core Features:
- Product management (CRUD, categories, SKU, inventory tracking)
- Sales checkout (barcode scan, cart, discounts, tax calculation)
- Payment integration (cash, credit card, mobile payment)
- Receipt generation (print + email)
- Order history and refunds
- Basic customer management (name, phone, purchase history)

User Roles:
- Admin (manage products, view reports)
- Cashier (process sales only)

UI/UX:
- Tablet-friendly interface
- Fast checkout flow (minimal clicks)
- Offline fallback mode

Non-functional:
- Handle 100 concurrent users
- Response time < 300ms
- Secure authentication (JWT)

Optional:
- Sales dashboard (daily revenue, top products)
- Multi-store support
```

Clarify the spec

```
/speckit.clarify
```


create plan

```
/speckit.plan

Goal:
- Validate POS checkout flow for small retail use
- Ensure system is usable on tablet in real-world scenario

Architecture:
- Frontend: React SPA (tablet-first UI)
- Backend: FastAPI (single monolithic service)
- Database: PostgreSQL

Core Features (POC Scope Only):
- Product list & search
- Add to cart
- Checkout (cash only)
- Simple order history
- Inventory deduction on purchase

Data Model:
- products (id, name, price, stock)
- orders (id, total_amount, created_at)
- order_items (order_id, product_id, quantity, price)

Key Logic:
- Checkout uses single DB transaction
- Deduct inventory when order is confirmed
- Prevent negative stock

API:
- REST only (no WebSocket)
- Basic endpoints: /products, /orders, /checkout

UI Flow:
- Home → Product list → Cart → Checkout → Success screen
- Optimized for touch (large buttons, minimal steps)

Non-functional:
- Response time < 500ms (local environment)
- No offline mode (manual testing only)

Deployment:
- Single server (Docker)
- Local or simple cloud VM

Out of Scope:
- Payments integration
- Multi-user roles
- Real-time sync
- Multi-store / SaaS
- Advanced reporting
```

Break the plan into tasks

```
./.specify/scripts/bash/setup-tasks.sh --json
```

Analyze for consistency
```
/speckit.analyze
```

Proceed to /speckit.implement to start building the POC.

```
/speckit.implement
```