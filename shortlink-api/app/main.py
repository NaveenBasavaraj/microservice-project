"""
FastAPI Application Entry Point.

This is the main file that creates and configures the FastAPI app.
All routes, middleware, and configurations are set up here.
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.routes import root, test


@asynccontextmanager
async def lifespan(_: FastAPI):
    """
    Runs application startup and shutdown logic.
    """
    print("🚀 ShortLink API is starting up...")
    print("📚 Documentation available at: http://127.0.0.1:8000/docs")
    yield
    print("👋 ShortLink API is shutting down...")



# Create the FastAPI application instance
app = FastAPI(
    title="ShortLink API",
    description="A URL shortening service built with FastAPI",
    version="0.1.0",
    docs_url="/docs",  # Swagger UI documentation
    redoc_url="/redoc",  # ReDoc documentation
    lifespan=lifespan,
)


# Include routers
# This connects all the routes from root.py to our main app
app.include_router(root.router, tags=["General"])
app.include_router(root.router, tags=["General"])
app.include_router(test.router, tags=["Testing"]) 