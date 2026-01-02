from fastapi import APIRouter
from datetime import datetime

router = APIRouter()


@router.get("/")
async def root():
    return {
        "app": "AI Demo API",
        "version": "0.1.0",
        "docs": "/docs",
    }


@router.get("/health")
async def health():
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
    }
