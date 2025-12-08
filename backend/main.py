from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.router import router

app = FastAPI(
    title="AI Demo API",
    version="0.1.0",
    docs_url="/docs",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api")
