# AI Demo App

An AI-powered chat application built with FastAPI and Next.js.

## Architecture

```
frontend/     # Next.js 14 with App Router
backend/      # FastAPI with async SQLAlchemy
config/       # Shared configuration
```

## Quick Start

```bash
# Start infrastructure
docker-compose up -d

# Backend
cd backend && pip install -r requirements.txt && uvicorn app.main:app --reload

# Frontend
cd frontend && npm install && npm run dev
```

## Team

- Sagar - Project Lead
- Swathi - Backend
- Zeeshan - Frontend
- Jay - Database
- Neha - AI/ML
