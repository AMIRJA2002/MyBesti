from fastapi import APIRouter
from core.database import db
from core.settings import settings

router = APIRouter()


@router.get("/")
async def health_check():
    try:
        await db.get_db().command('ping')
        db_status = "connected"
    except Exception as e:
        db_status = f"disconnected: {str(e)}"
    
    return {
        "status": "ok",
        "app_name": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "environment": settings.ENVIRONMENT,
        "database": db_status
    }
