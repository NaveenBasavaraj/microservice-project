"""
FastAPI Application Entry Point.

This is the main file that creates and configures the FastAPI app.
All routes, middleware, and configurations are set up here.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import root
from app.config import settings  # ← Import our settings!
from app.database import check_db_connection


# Create the FastAPI application instance using config values
app = FastAPI(
    title=settings.app_name,              # ← From config!
    description="A URL shortening service built with FastAPI",
    version=settings.app_version,         # ← From config!
    debug=settings.debug,                 # ← From config!
    docs_url="/docs",
    redoc_url="/redoc"
)


# Add CORS middleware (allows frontend apps to call our API)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.get_allowed_origins_list(),  # ← From config!
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)


# Include routers
app.include_router(root.router, tags=["General"])


@app.on_event("startup")
async def startup_event():
    """
    Runs when the application starts.
    """
    print(f"🚀 {settings.app_name} v{settings.app_version} is starting up...")
    print(f"🐛 Debug mode: {settings.debug}")
    print(f"📚 Documentation: http://127.0.0.1:8000/docs")
    if settings.debug:
        print(f"⚙️  Database: {settings.database_url[:30]}...")
    if check_db_connection():
        print("✅ Database connection successful")
    else:
        print("⚠️  Database connection failed (check Docker/PostgreSQL)")


@app.on_event("shutdown")
async def shutdown_event():
    """
    Runs when the application shuts down.
    """
    print(f"👋 {settings.app_name} is shutting down...")