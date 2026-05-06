# Tasks: Cloud POS Web Application

**Input**: Design documents from `/specs/001-cloud-pos/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Basic unit and integration tests are included for core backend logic and frontend components to validate POC functionality.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Backend**: `backend/app/` for API code, `backend/` for config
- **Frontend**: `frontend/src/` for React components and pages
- **Tests**: `tests/backend/` for backend tests, `tests/frontend/` for frontend tests

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create backend project structure per implementation plan
- [ ] T002 Create frontend project structure per implementation plan
- [ ] T003 Setup Docker Compose configuration for local development
- [ ] T004 [P] Configure backend dependencies and requirements.txt
- [ ] T005 [P] Configure frontend dependencies and package.json

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T006 Setup PostgreSQL database connection and session management in backend/app/db.py
- [ ] T007 Create Product model in backend/app/models/product.py
- [ ] T008 Create Order model in backend/app/models/order.py
- [ ] T009 Create OrderItem model in backend/app/models/order_item.py
- [ ] T010 Setup database schema initialization and sample data seeding
- [ ] T011 Create base API router structure in backend/app/main.py
- [ ] T012 Configure CORS and basic middleware for tablet frontend access
- [ ] T013 [P] Implement JWT authentication with role-based access (admin/cashier) in backend/app/auth.py
- [ ] T014 [P] Add user role enforcement middleware for protected endpoints

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Product and Inventory Management (Priority: P1) 🎯 MVP

**Goal**: Enable admin to manage products and inventory for accurate checkout

**Independent Test**: Verify products can be listed and inventory levels are tracked

### Tests for User Story 1 ⚠️

- [ ] T017 [P] [US1] Unit test for Product model validation in tests/backend/unit/test_product_model.py
- [ ] T018 [P] [US1] Integration test for product CRUD operations in tests/backend/integration/test_product_api.py

### Implementation for User Story 1

- [ ] T017 [US1] Implement GET /products endpoint in backend/app/api/products.py
- [ ] T018 [US1] Add product search and pagination to GET /products
- [ ] T019 [US1] Implement POST /products for creating new products
- [ ] T020 [US1] Implement PUT /products/{id} for updating products
- [ ] T021 [US1] Implement DELETE /products/{id} for removing products
- [ ] T022 [US1] Create ProductList component in frontend/src/components/ProductList.tsx
- [ ] T023 [US1] Create ProductForm component for add/edit in frontend/src/components/ProductForm.tsx
- [ ] T024 [US1] Create AdminPage for product management in frontend/src/pages/AdminPage.tsx
- [ ] T025 [US1] Integrate product API calls in frontend/src/services/api.ts

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Fast Tablet Checkout (Priority: P1)

**Goal**: Enable cashier to complete sales with cart, checkout, and inventory deduction

**Independent Test**: Verify checkout completes transaction and updates inventory

### Tests for User Story 2 ⚠️

- [ ] T026 [P] [US2] Unit test for checkout transaction logic in tests/backend/unit/test_checkout_service.py
- [ ] T027 [P] [US2] Integration test for POST /checkout endpoint in tests/backend/integration/test_checkout_api.py

### Implementation for User Story 2

- [ ] T028 [US2] Implement POST /checkout endpoint with transaction in backend/app/api/checkout.py
- [ ] T029 [US2] Add inventory validation and deduction in checkout service
- [ ] T030 [US2] Create Cart component for item selection in frontend/src/components/Cart.tsx
- [ ] T031 [US2] Create CheckoutPage with total calculation in frontend/src/pages/CheckoutPage.tsx
- [ ] T032 [US2] Create SuccessPage for order confirmation in frontend/src/pages/SuccessPage.tsx
- [ ] T033 [US2] Implement cart state management in frontend/src/services/cart.ts
- [ ] T034 [US2] Add checkout API integration in frontend/src/services/api.ts

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Order History and Refunds (Priority: P2)

**Goal**: Enable viewing past orders and processing refunds

**Independent Test**: Verify order history displays and refunds update status

### Tests for User Story 3 ⚠️

- [ ] T035 [P] [US3] Unit test for order status updates in tests/backend/unit/test_order_model.py
- [ ] T036 [P] [US3] Integration test for orders API in tests/backend/integration/test_orders_api.py

### Implementation for User Story 3

- [ ] T039 [US3] Implement GET /orders endpoint in backend/app/api/orders.py
- [ ] T040 [US3] Implement GET /orders/{id} for order details
- [ ] T041 [US3] Add order search and pagination to GET /orders
- [ ] T042 [US3] Implement refund logic for order status updates
- [ ] T043 [US3] Create OrderHistory component in frontend/src/components/OrderHistory.tsx
- [ ] T044 [US3] Create OrderDetail component for viewing orders
- [ ] T045 [US3] Add refund functionality to order details
- [ ] T046 [US3] Integrate orders API in frontend/src/services/api.ts

**Checkpoint**: At this point, User Stories 1, 2, AND 3 should work independently

---

## Phase 6: User Story 5 - Offline Fallback for Checkout (Priority: P2)

**Goal**: Enable cash checkout when offline with local queueing

**Independent Test**: Verify offline checkout queues and syncs on reconnection

### Implementation for User Story 5

- [ ] T057 [US5] Add offline detection in frontend/src/services/api.ts
- [ ] T046 [US5] Implement local storage queue for offline orders
- [ ] T047 [US5] Add sync mechanism for queued orders on reconnection
- [ ] T048 [US5] Update checkout flow to handle offline cash payments
- [ ] T049 [US5] Add offline status indicator in frontend UI

**Checkpoint**: All user stories should now be independently functional

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T050 [P] Add error handling and user feedback across frontend components
- [ ] T051 [P] Implement basic tablet-responsive styling in frontend/src/styles/
- [ ] T052 [P] Add loading states and progress indicators
- [ ] T053 Run end-to-end checkout flow validation
- [ ] T054 Update quickstart.md with Docker Compose instructions
- [ ] T055 Add basic performance monitoring for API endpoints (response time logging)
- [ ] T056 Add concurrency testing for 100+ simulated users on checkout endpoints

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - Depends on US1 for product data
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - Depends on US2 for order data
- **User Story 5 (P2)**: Can start after Foundational (Phase 2) - Depends on US2 for checkout flow

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together:
Task: "Unit test for Product model validation in tests/backend/unit/test_product_model.py"
Task: "Integration test for product CRUD operations in tests/backend/integration/test_product_api.py"

# Launch all models for User Story 1 together:
Task: "Create ProductList component in frontend/src/components/ProductList.tsx"
Task: "Create ProductForm component for add/edit in frontend/src/components/ProductForm.tsx"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 5 → Test independently → Deploy/Demo
6. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3 + 5
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence