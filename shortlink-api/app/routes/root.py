"""
Root routes for the application.
These are general endpoints like health checks and welcome messages.
"""

from fastapi import APIRouter

# Create a router - this is like a mini FastAPI app
# We use routers to organize related endpoints
router = APIRouter()


@router.get("/")
def read_root():
    """
    Welcome endpoint.
    Returns basic information about the API.
    """
    return {
        "message": "Welcome to ShortLink API! 🚀",
        "version": "0.1.0",
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
        "service": "ShortLink API",
        "version": "0.1.0"
    }