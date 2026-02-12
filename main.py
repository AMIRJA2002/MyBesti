from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from beanie import init_beanie

from core.settings import settings
from core.database import db
from core.telegram import telegram
from api.v1.router import api_router
from users.models import User


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    await db.connect_db()
    await init_beanie(database=db.get_db(), document_models=[User])
    await telegram.connect()
    yield
    # Shutdown
    await db.close_db()
    await telegram.disconnect()


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    debug=settings.DEBUG,
    lifespan=lifespan
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(api_router, prefix="/api/v1")


@app.get("/")
async def root():
    return {
        "message": f"Welcome to {settings.APP_NAME}",
        "version": settings.APP_VERSION,
        "docs": "/docs"
    }
