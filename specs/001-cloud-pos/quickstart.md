# Quickstart: Cloud POS Web Application POC

## Prerequisites
- Python 3.11
- Node.js 18+ / npm or pnpm
- Docker and Docker Compose (for containerized deployment)
- PostgreSQL database or local Docker PostgreSQL instance

## Local Development

### Backend
1. Create a Python virtual environment:
   ```bash
   cd backend
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. Install backend dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure environment variables in `backend/.env` or your shell:
   ```bash
   DATABASE_URL=postgresql://user:password@localhost:5432/cloudpos
   SECRET_KEY=change-me
   ```
4. Run database migrations and start the service:
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

### Frontend
1. Install dependencies:
   ```bash
   cd frontend
   npm install
   ```
2. Start the frontend development server:
   ```bash
   npm run dev
   ```
3. Open the browser on a tablet or tablet emulator at the development URL (for example `http://localhost:5173`).

## Docker Deployment

1. Build the backend image:
   ```bash
   docker build -t cloud-pos-backend ./backend
   ```
2. Build the frontend image:
   ```bash
   docker build -t cloud-pos-frontend ./frontend
   ```
3. Start required containers and the database. If using Docker Compose, run:
   ```bash
   docker compose up --build
   ```
4. Confirm the backend is reachable at `http://localhost:8000` and the frontend at its configured host.

## Validation
- Verify product list loads quickly on a tablet screen
- Add items to the cart, complete a cash-only checkout, and confirm the order appears in history
- Confirm inventory updates when an order is submitted
- Ensure the checkout flow remains simple and touch-friendly

## Notes
- This POC intentionally excludes offline mode and payment gateway integration
- If PostgreSQL is unavailable locally, use Docker to run a temporary database instance
