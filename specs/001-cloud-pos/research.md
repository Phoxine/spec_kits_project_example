# Research: Cloud POS Web Application

## Decision: React SPA + FastAPI + PostgreSQL
- Rationale: This combination delivers fast iteration for a tablet-first POC with a clean separation between frontend UI and backend transaction logic.
- Alternatives considered: Next.js or full-stack frameworks, but those introduce additional routing and server rendering complexity for a simple checkout demo.

## Decision: PostgreSQL as the data store
- Rationale: Inventory, orders, and checkout transactions benefit from relational integrity, ACID transactions, and straightforward SQL queries.
- Alternatives considered: SQLite for local demos or NoSQL for flexibility. Rejected because PostgreSQL better supports concurrent checkout workloads and real transactional guarantees.

## Decision: Cash-only checkout for POC
- Rationale: This avoids payment provider integration, security/PIN handling, and offline settlement complexities while preserving the checkout flow.
- Alternatives considered: Include card/mobile payment or mock integration. Rejected because payments are out of scope for this POC.

## Decision: REST API only
- Rationale: A REST contract supports the SPA cleanly and keeps the interface simple for product list, order history, and checkout interactions.
- Alternatives considered: GraphQL or WebSocket. Rejected because REST is sufficient for the required flow and reduces implementation overhead.

## Decision: Single Docker-deployed backend service
- Rationale: Single-server deployment is easiest for local and simple cloud VM testing, and it keeps the architecture aligned with the POC scope.
- Alternatives considered: Separate microservices or serverless. Rejected due to unnecessary complexity for a small retail POC.

## Decision: No offline mode for this phase
- Rationale: The user request explicitly states manual testing only and reduces risk by keeping the POC online-only.
- Alternatives considered: offline queueing or sync support. Rejected because it adds significant client-side state and recovery complexity.
