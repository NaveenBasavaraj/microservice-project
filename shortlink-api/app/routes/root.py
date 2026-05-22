"""
Root routes for the application.
These are general endpoints like health checks and welcome messages.
"""

from fastapi import APIRouter
from app.config import settings  # ← Import settings!

# Create a router
router = APIRouter()


@router.get("/")
def read_root():
    """
    Welcome endpoint.
    Returns basic information about the API.
    """
    return {
        "message": f"Welcome to {settings.app_name}! 🚀",  # ← From config!
        "version": settings.app_version,                    # ← From config!
        "docs": "/docs",
        "health": "/health"
    }


@router.get("/health")
def health_check():
    """
    Health check endpoint.
    Used by monitoring tools to verify the service is running.
    """
    return {
        "status": "healthy",
        "service": settings.app_name,      # ← From config!
        "version": settings.app_version,   # ← From config!
        "debug": settings.debug            # ← From config!
    }