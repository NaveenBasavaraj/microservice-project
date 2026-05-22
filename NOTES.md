# 🎯 **Phase 1: Minimal FastAPI App**

## **Goal**
Create a single Python file that runs FastAPI and shows "Hello World" in your browser.

---

## 📖 **Mini Theory: What is FastAPI?**

FastAPI is a **web framework** for Python. Think of it as a tool that helps you create websites and APIs without dealing with low-level networking code.

**What's an API?** It's a way for programs to talk to each other over the internet. When you visit a website, your browser is talking to an API.

**Why FastAPI?**
- Super fast (as fast as Node.js)
- Easy to learn
- Automatic documentation
- Type hints make code safer

---

## 💻 **Let's Code!**

### **Step 1: Create Your Project Folder**

Open your terminal and run:

```bash
mkdir shortlink-api
cd shortlink-api
```

---

### **Step 2: Create a Virtual Environment**

**What's a virtual environment?** It's like a separate Python installation just for this project. It keeps your project's packages isolated from other projects.

```bash
# Create virtual environment
python -m venv venv

# Activate it (Windows)
venv\Scripts\activate

# Activate it (Mac/Linux)
source venv/bin/activate
```

You'll see `(venv)` appear in your terminal. This means it's active! ✅

---

### **Step 3: Install FastAPI**

```bash
pip install fastapi
pip install "uvicorn[standard]"
```

**What did we just install?**
- `fastapi`: The web framework
- `uvicorn`: A server that runs your FastAPI app (like hitting "play" on a video)

---

### **Step 4: Create `main.py`**

Create a file called `main.py` and add this code:

```python name=main.py
# Import FastAPI - this is the main tool we'll use
from fastapi import FastAPI

# Create an "app" - this is your web application
app = FastAPI()

# Create a "route" - this is a URL endpoint
# When someone visits "/", this function runs
@app.get("/")
def read_root():
    """
    This is our first endpoint!
    It returns a simple JSON message.
    """
    return {"message": "Hello, World! 🚀"}

# Another endpoint - just to see how easy it is
@app.get("/health")
def health_check():
    """
    Health check endpoint.
    Useful to check if the API is running.
    """
    return {"status": "healthy", "service": "ShortLink API"}
```

---

### **📝 Code Explanation (Line by Line)**

**Line 2:** `from fastapi import FastAPI`
- We're bringing FastAPI into our code so we can use it

**Line 5:** `app = FastAPI()`
- We create an instance of FastAPI
- This `app` object will hold all our routes and configuration

**Line 9:** `@app.get("/")`
- This is a **decorator** - it connects a URL to a function
- `get` means this responds to GET requests (like when you type a URL in a browser)
- `"/"` is the path - the homepage

**Line 10-15:** The function
- When someone visits `/`, FastAPI calls this function
- It returns a dictionary (Python dict)
- FastAPI automatically converts it to JSON

**Line 18-24:** Second endpoint
- Same pattern, different URL (`/health`)
- This is a common pattern - most APIs have a health check endpoint

---

## ✅ **Step 5: Run Your App!**

In your terminal (with `venv` activated), run:

```bash
uvicorn main:app --reload
```

**What does this command mean?**
- `uvicorn`: The server program
- `main`: The name of your Python file (main.py)
- `app`: The variable name in your file
- `--reload`: Auto-restart when you change code (super useful for development!)

You should see output like this:

```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [12345] using StatReloader
INFO:     Started server process [12346]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

---

## 🧪 **Step 6: Test It!**

### **Test 1: Browser**
Open your browser and go to:
- `http://127.0.0.1:8000/` - You should see:
  ```json
  {"message":"Hello, World! 🚀"}
  ```

- `http://127.0.0.1:8000/health` - You should see:
  ```json
  {"status":"healthy","service":"ShortLink API"}
  ```

### **Test 2: Automatic Documentation** (🤯 Mind-blowing!)
Go to: `http://127.0.0.1:8000/docs`

**BOOM!** 💥 FastAPI automatically created interactive API documentation for you! You can click "Try it out" and test your endpoints right there.

Also try: `http://127.0.0.1:8000/redoc` - Alternative documentation style.

---

## 🎓 **What You Just Learned**

✅ How to create a FastAPI application  
✅ What routes/endpoints are  
✅ How decorators work (`@app.get()`)  
✅ FastAPI automatically converts Python dicts to JSON  
✅ FastAPI generates interactive documentation for FREE  
✅ How to run a development server with hot-reload  

---

## 🔍 **Try These Experiments**

Before moving to Phase 2, try modifying your code:

**Experiment 1:** Add a new endpoint
```python
@app.get("/about")
def about():
    return {"project": "URL Shortener", "version": "0.1.0", "author": "Your Name"}
```

**Experiment 2:** Change the message
```python
@app.get("/")
def read_root():
    return {"message": "Welcome to ShortLink API!", "endpoints": ["/", "/health", "/about"]}
```

**Experiment 3:** Use path parameters
```python
@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}! 👋"}
```
Test this at: `http://127.0.0.1:8000/greet/Naveen`

---

## 📦 **Save Your Dependencies**

Run this to save what packages you installed:

```bash
pip freeze > requirements.txt
```

**What's this for?** Later, anyone (including you on another computer) can install all dependencies with:
```bash
pip install -r requirements.txt
```

---

## 🎯 **Phase 1 Complete! 🎉**

**What you have now:**
- ✅ A working FastAPI application
- ✅ Two endpoints that return JSON
- ✅ Auto-generated documentation
- ✅ Hot-reload development server

**Current project structure:**
```
shortlink-api/
├── venv/               (virtual environment - don't touch this)
├── main.py            (your application)
└── requirements.txt   (list of packages)
```

---

## 🔗 **Coming in Phase 2: Project Structure**

Right now everything is in one file. That's fine for hello world, but we need to organize:
- Where do routes go?
- Where do database models go?
- Where do we put configuration?

We'll create a proper folder structure that scales as the project grows.

---

## 📸 **Before Moving On - Checklist**

- [ ] FastAPI app runs without errors
- [ ] You can see "Hello World" in browser
- [ ] You visited `/docs` and saw interactive documentation
- [ ] You tried at least ONE experiment (added an endpoint or changed a message)
- [ ] You understand what `@app.get()` does

---

# 🎯 **Phase 2: Project Structure**

## **Goal**
Organize our code into folders and files so it's easy to find things and scale the project.

---

## 📖 **Mini Theory: Why Do We Need Structure?**

Right now, everything is in `main.py`. That works for 20 lines of code, but imagine when we have:
- 10 different endpoints
- Database models
- Authentication logic
- Configuration
- Utility functions

**All in one file?** 😱 It would be a 500-line mess!

**Professional projects** organize code into logical folders:
- **Routes** (endpoints) go in one place
- **Database models** go in another
- **Configuration** has its own spot
- **Business logic** is separate from routing

This is called **separation of concerns** - each file/folder has ONE job.

---

## 📁 **The Structure We'll Build**

```
shortlink-api/
├── venv/                    (virtual environment - ignore this)
├── app/                     (our main application folder)
│   ├── __init__.py         (makes 'app' a Python package)
│   ├── main.py             (application entry point)
│   ├── config.py           (settings - we'll add this in Phase 3)
│   ├── database.py         (database connection - Phase 5)
│   ├── models/             (database models - Phase 6)
│   │   └── __init__.py
│   ├── routes/             (API endpoints)
│   │   ├── __init__.py
│   │   └── root.py         (our hello world endpoints)
│   └── schemas/            (data validation - Phase 9)
│       └── __init__.py
├── requirements.txt
└── .gitignore              (tells git what NOT to upload)
```

**Why this structure?**
- `app/` contains ALL application code
- `routes/` will hold all our endpoints (we'll have many!)
- `models/` will hold database table definitions
- `schemas/` will validate incoming data
- Everything is organized by PURPOSE

---

## 💻 **Let's Build It!**

### **Step 1: Create the Folder Structure**

In your terminal (in the `shortlink-api` folder):

```bash
# Create the folders
mkdir app
mkdir app/routes
mkdir app/models
mkdir app/schemas

# Create __init__.py files (makes folders into Python packages)
# Windows
type nul > app/__init__.py
type nul > app/routes/__init__.py
type nul > app/models/__init__.py
type nul > app/schemas/__init__.py

# Mac/Linux
touch app/__init__.py
touch app/routes/__init__.py
touch app/models/__init__.py
touch app/schemas/__init__.py
```

---

### **Step 2: Move Routes to `app/routes/root.py`**

Create a new file: `app/routes/root.py`

```python name=app/routes/root.py
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
```

**📝 What's new here?**

**Line 7:** `from fastapi import APIRouter`
- `APIRouter` is like a mini FastAPI app
- We use multiple routers to organize endpoints by feature
- Later we'll have `auth.py`, `links.py`, etc.

**Line 11:** `router = APIRouter()`
- Create a router instance
- This will hold all endpoints in this file

**Line 14:** `@router.get("/")` instead of `@app.get("/")`
- We're attaching endpoints to the router, not directly to the app
- The main app will "include" all routers

---

### **Step 3: Create New `app/main.py`**

Create: `app/main.py`

```python name=app/main.py
"""
FastAPI Application Entry Point.

This is the main file that creates and configures the FastAPI app.
All routes, middleware, and configurations are set up here.
"""

from fastapi import FastAPI
from app.routes import root

# Create the FastAPI application instance
app = FastAPI(
    title="ShortLink API",
    description="A URL shortening service built with FastAPI",
    version="0.1.0",
    docs_url="/docs",  # Swagger UI documentation
    redoc_url="/redoc"  # ReDoc documentation
)


# Include routers
# This connects all the routes from root.py to our main app
app.include_router(root.router, tags=["General"])


@app.on_event("startup")
async def startup_event():
    """
    Runs when the application starts.
    Useful for initializing database connections, loading config, etc.
    """
    print("🚀 ShortLink API is starting up...")
    print("📚 Documentation available at: http://127.0.0.1:8000/docs")


@app.on_event("shutdown")
async def shutdown_event():
    """
    Runs when the application shuts down.
    Useful for closing database connections, cleaning up resources, etc.
    """
    print("👋 ShortLink API is shutting down...")
```

**📝 What's happening here?**

**Lines 12-18:** `FastAPI()` with parameters
- `title`: Shows up in the docs
- `description`: Explains what your API does
- `version`: Track your API version
- `docs_url` & `redoc_url`: Where documentation lives

**Line 23:** `app.include_router()`
- This **connects** the router from `root.py` to our main app
- `tags=["General"]` groups these endpoints in the docs
- We'll add more routers later (auth, links, etc.)

**Lines 26-32:** `@app.on_event("startup")`
- This function runs ONCE when the server starts
- Useful for database connections, loading config, etc.
- Right now it just prints a message

**Lines 35-41:** `@app.on_event("shutdown")`
- Runs when you stop the server (Ctrl+C)
- Useful for cleanup (closing DB connections, etc.)

---

### **Step 4: Delete Old `main.py`**

You still have the old `main.py` in the root folder. Delete it or rename it to `main_old.py` for reference.

```bash
# Rename it (safe)
mv main.py main_old.py

# Or delete it (if you're confident)
rm main.py
```

---

### **Step 5: Update How We Run the App**

Now our main app is in `app/main.py`, so the command changes:

```bash
# OLD command (Phase 1)
# uvicorn main:app --reload

# NEW command (Phase 2)
uvicorn app.main:app --reload
```

**What changed?**
- `main:app` → `app.main:app`
- This means: "In the `app` folder, in the `main.py` file, use the `app` variable"

---

## ✅ **Step 6: Test It!**

Run your app:

```bash
uvicorn app.main:app --reload
```

**Test in browser:**
- `http://127.0.0.1:8000/` - Should work! ✅
- `http://127.0.0.1:8000/health` - Should work! ✅
- `http://127.0.0.1:8000/docs` - Check if endpoints are tagged as "General" ✅

**Look at your terminal** - you should see:
```
🚀 ShortLink API is starting up...
📚 Documentation available at: http://127.0.0.1:8000/docs
```

When you press `Ctrl+C`, you should see:
```
👋 ShortLink API is shutting down...
```

---

## 📦 **Step 7: Add `.gitignore`**

Create a file called `.gitignore` in the root folder:

```text name=.gitignore
# Python virtual environment
venv/
env/
ENV/

# Python cache files
__pycache__/
*.py[cod]
*$py.class
*.so

# Environment variables (NEVER commit secrets!)
.env
.env.local

# IDE files
.vscode/
.idea/
*.swp
*.swo

# Database files (we'll use Docker, but just in case)
*.db
*.sqlite3

# OS files
.DS_Store
Thumbs.db

# pytest cache
.pytest_cache/

# Coverage reports
htmlcov/
.coverage
```

**Why `.gitignore`?**
- Tells Git what NOT to upload to GitHub
- `venv/` is HUGE and user-specific - never upload it!
- `.env` will contain secrets (passwords, API keys) - never upload it!
- `__pycache__/` is auto-generated - no need to track it

---

## 🎓 **What You Just Learned**

✅ **Project structure** - organize code by purpose  
✅ **APIRouter** - modular way to organize endpoints  
✅ **`app.include_router()`** - connect routers to main app  
✅ **Startup/shutdown events** - run code when app starts/stops  
✅ **`.gitignore`** - keep secrets and junk out of Git  
✅ **Python packages** - `__init__.py` makes folders importable  

---

## 🔍 **Understanding `__init__.py`**

**Why do we need empty `__init__.py` files?**

In Python, a folder needs `__init__.py` to be treated as a **package** (importable module).

Without it:
```python
from app.routes import root  # ❌ ERROR: app is not a package
```

With it:
```python
from app.routes import root  # ✅ WORKS!
```

**Most of the time it's empty**, but you CAN put code in it. We'll use this later!

---

## 📂 **Your Project Now Looks Like This**

```
shortlink-api/
├── venv/
├── app/
│   ├── __init__.py
│   ├── main.py             ← Application entry point
│   ├── routes/
│   │   ├── __init__.py
│   │   └── root.py         ← Hello world endpoints
│   ├── models/
│   │   └── __init__.py
│   └── schemas/
│       └── __init__.py
├── requirements.txt
├── .gitignore
└── main_old.py (if you kept it)
```

---

## 🧪 **Try These Experiments**

**Experiment 1:** Add a new route file

Create `app/routes/test.py`:
```python
from fastapi import APIRouter

router = APIRouter()

@router.get("/test")
def test_endpoint():
    return {"message": "This is a test endpoint!"}
```

Then add it to `app/main.py`:
```python
from app.routes import root, test

app.include_router(root.router, tags=["General"])
app.include_router(test.router, tags=["Testing"])  # Add this line
```

Visit: `http://127.0.0.1:8000/test` and `http://127.0.0.1:8000/docs`

**Experiment 2:** Add a prefix to a router

In `app/main.py`, change:
```python
app.include_router(test.router, prefix="/api/v1", tags=["Testing"])
```

Now the endpoint is at: `http://127.0.0.1:8000/api/v1/test`

---

## 🎯 **Phase 2 Complete! 🎉**

**What you have now:**
- ✅ Professional project structure
- ✅ Organized routes in separate files
- ✅ Modular code with APIRouter
- ✅ Startup/shutdown event handlers
- ✅ `.gitignore` to protect secrets

**You're now coding like a professional backend developer!** 🚀

---

## 🔗 **Coming in Phase 3: Configuration**

We'll create a `config.py` file to manage settings like:
- Database URLs
- Secret keys
- API settings
- Environment variables

**Rule:** NEVER hardcode passwords or API keys in your code!

---

## 📸 **Before Moving On - Checklist**

- [ ] App runs with `uvicorn app.main:app --reload`
- [ ] Browser shows endpoints working
- [ ] You see the startup message in terminal
- [ ] You understand why we use `APIRouter`
- [ ] You understand what `__init__.py` does
- [ ] `.gitignore` is created

---


# 🎯 **Phase 3: Configuration**

## **Goal**
Never hardcode values! Use environment variables and a config system to manage settings safely.

---

## 📖 **Mini Theory: Why Configuration Management?**

**Bad code (what we DON'T want):**
```python
# ❌ NEVER DO THIS!
DATABASE_URL = "postgresql://admin:password123@localhost:5432/mydb"
SECRET_KEY = "super-secret-key-12345"
API_KEY = "sk_live_abc123xyz"
```

**Why is this bad?**
1. **Security risk** - Passwords visible in code
2. **Hard to change** - Need to edit code to change settings
3. **No flexibility** - Can't have different settings for dev/staging/production
4. **Git disaster** - You'll accidentally commit secrets to GitHub!

**The Solution: Environment Variables**

Environment variables are values stored OUTSIDE your code:
- Development: Use `.env` file (local only, never committed)
- Production: Set them in your hosting platform (Heroku, AWS, etc.)

---

## 🔧 **What We'll Build**

1. A `.env` file for local secrets
2. A `config.py` file that reads environment variables
3. Type-safe configuration using Pydantic

---

## 💻 **Let's Code!**

### **Step 1: Install Required Packages**

```bash
pip install python-dotenv pydantic-settings
```

**What are these?**
- `python-dotenv`: Reads `.env` files and loads them into environment variables
- `pydantic-settings`: Validates and manages settings with type safety

---

### **Step 2: Create `.env` File**

Create a file called `.env` in the ROOT folder (same level as `app/`):

```text name=.env
# Application Settings
APP_NAME="ShortLink API"
APP_VERSION="0.1.0"
DEBUG=True

# API Settings
API_V1_PREFIX="/api/v1"

# Database Settings (we'll use this in Phase 4)
DATABASE_URL="postgresql://postgres:postgres@localhost:5432/shortlink_db"

# Security Settings (we'll use this in Phase 12)
SECRET_KEY="your-super-secret-key-change-this-in-production"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30

# CORS Settings (Cross-Origin Resource Sharing)
ALLOWED_ORIGINS="http://localhost:3000,http://localhost:8000"
```

**📝 Important Notes:**

- This file is in `.gitignore` - it will NEVER be committed to Git! ✅
- Each developer has their own `.env` file
- Production servers have their own environment variables (not files!)

---

### **Step 3: Create `.env.example`**

Create `.env.example` (this WILL be committed to Git):

```text name=.env.example
# Application Settings
APP_NAME="ShortLink API"
APP_VERSION="0.1.0"
DEBUG=True

# API Settings
API_V1_PREFIX="/api/v1"

# Database Settings
DATABASE_URL="postgresql://user:password@localhost:5432/dbname"

# Security Settings
SECRET_KEY="change-this-to-a-random-string"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30

# CORS Settings
ALLOWED_ORIGINS="http://localhost:3000,http://localhost:8000"
```

**Why `.env.example`?**
- Shows other developers what variables are needed
- No real passwords/secrets - just placeholders
- Safe to commit to Git
- New developers copy this to `.env` and fill in real values

---

### **Step 4: Create `app/config.py`**

Create: `app/config.py`

```python name=app/config.py
"""
Configuration Management.

This module handles all application settings using environment variables.
It uses Pydantic for validation and type safety.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.
    
    Pydantic will automatically:
    - Load values from .env file
    - Validate types (str, int, bool, etc.)
    - Provide default values
    - Raise errors if required values are missing
    """
    
    # Application Settings
    app_name: str = "ShortLink API"
    app_version: str = "0.1.0"
    debug: bool = True
    
    # API Settings
    api_v1_prefix: str = "/api/v1"
    
    # Database Settings
    database_url: str
    
    # Security Settings
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    
    # CORS Settings (Cross-Origin Resource Sharing)
    allowed_origins: str = "http://localhost:3000"
    
    # Configure how Pydantic loads settings
    model_config = SettingsConfigDict(
        env_file=".env",           # Load from .env file
        env_file_encoding="utf-8", # File encoding
        case_sensitive=False,      # DATABASE_URL = database_url (flexible)
        extra="ignore"             # Ignore extra variables in .env
    )
    
    def get_allowed_origins_list(self) -> List[str]:
        """
        Convert comma-separated origins string to a list.
        Example: "http://localhost:3000,http://localhost:8000" 
                 -> ["http://localhost:3000", "http://localhost:8000"]
        """
        return [origin.strip() for origin in self.allowed_origins.split(",")]


# Create a single instance of settings
# This will be imported throughout the application
settings = Settings()


# Print loaded settings (for debugging - remove in production!)
if __name__ == "__main__":
    print("🔧 Configuration Loaded:")
    print(f"  App Name: {settings.app_name}")
    print(f"  Version: {settings.app_version}")
    print(f"  Debug Mode: {settings.debug}")
    print(f"  API Prefix: {settings.api_v1_prefix}")
    print(f"  Database URL: {settings.database_url[:30]}...")  # Don't print full URL!
    print(f"  Allowed Origins: {settings.get_allowed_origins_list()}")
```

**📝 Let's Break This Down:**

**Lines 8-9:** Imports
- `BaseSettings`: Pydantic's base class for settings management
- `SettingsConfigDict`: Configuration for how settings are loaded

**Lines 13-21:** The `Settings` class
- Inherits from `BaseSettings`
- Each attribute becomes a configurable setting
- Type hints (`str`, `int`, `bool`) provide validation

**Lines 23-26:** Simple settings with defaults
- If not in `.env`, use these default values
- `debug: bool = True` means "debug" is a boolean, default is True

**Line 32:** `database_url: str`
- NO default value = REQUIRED
- App won't start if this is missing from `.env`

**Lines 43-49:** `model_config`
- Tells Pydantic HOW to load settings
- `env_file=".env"` - where to find values
- `case_sensitive=False` - DATABASE_URL matches database_url
- `extra="ignore"` - ignore unknown variables (won't crash if you add extra stuff to .env)

**Lines 51-57:** Helper method
- Converts comma-separated string to list
- We'll use this for CORS (allowing frontend apps to call our API)

**Line 61:** `settings = Settings()`
- Create ONE instance
- This will be imported everywhere: `from app.config import settings`

---

### **Step 5: Update `app/main.py` to Use Config**

Update: `app/main.py`

```python name=app/main.py
"""
FastAPI Application Entry Point.

This is the main file that creates and configures the FastAPI app.
All routes, middleware, and configurations are set up here.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import root
from app.config import settings  # ← Import our settings!


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


@app.on_event("shutdown")
async def shutdown_event():
    """
    Runs when the application shuts down.
    """
    print(f"👋 {settings.app_name} is shutting down...")
```

**📝 What Changed?**

**Line 9:** Added `CORSMiddleware` import
- CORS = Cross-Origin Resource Sharing
- Allows your API to be called from web browsers on different domains

**Line 11:** Import our settings!

**Lines 16-19:** Use config values
- `title=settings.app_name` instead of hardcoded string
- Easy to change in `.env` file!

**Lines 25-32:** CORS middleware
- Uses `allowed_origins` from config
- Allows specified domains to call your API
- Important when you build a frontend (React, Vue, etc.)

**Lines 43-47:** Print config on startup
- Shows what configuration is being used
- Only shows first 30 chars of database URL (security!)

---

### **Step 6: Update `app/routes/root.py` to Use Config**

Update: `app/routes/root.py`

```python name=app/routes/root.py
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
```

---

## ✅ **Step 7: Test Configuration**

### **Test 1: Verify Config Loads**

Run this command to test config loading:

```bash
python -m app.config
```

You should see:
```
🔧 Configuration Loaded:
  App Name: ShortLink API
  Version: 0.1.0
  Debug Mode: True
  API Prefix: /api/v1
  Database URL: postgresql://postgres:postgre...
  Allowed Origins: ['http://localhost:3000', 'http://localhost:8000']
```

If you see an error about `database_url`, check your `.env` file!

---

### **Test 2: Run the App**

```bash
uvicorn app.main:app --reload
```

Check the startup message - it should show config values:
```
🚀 ShortLink API v0.1.0 is starting up...
🐛 Debug mode: True
📚 Documentation: http://127.0.0.1:8000/docs
⚙️  Database: postgresql://postgres:postgre...
```

---

### **Test 3: Test Endpoints**

Visit:
- `http://127.0.0.1:8000/` - Should show app name from config
- `http://127.0.0.1:8000/health` - Should show debug status

---

### **Test 4: Change a Setting**

Edit `.env` and change:
```
APP_NAME="My Awesome URL Shortener"
DEBUG=False
```

Restart the server (Ctrl+C, then `uvicorn app.main:app --reload`)

Visit `http://127.0.0.1:8000/` - the name should be different!

---

## 📦 **Step 8: Update `requirements.txt`**

```bash
pip freeze > requirements.txt
```

Your `requirements.txt` should now include:
```
fastapi
uvicorn[standard]
python-dotenv
pydantic-settings
```

---

## 🎓 **What You Just Learned**

✅ **Environment variables** - store secrets outside code  
✅ **`.env` files** - local configuration that's never committed  
✅ **`.env.example`** - template for other developers  
✅ **Pydantic Settings** - type-safe configuration management  
✅ **CORS** - allow frontends to call your API  
✅ **Configuration centralization** - one place to manage all settings  
✅ **Security best practices** - never hardcode secrets!  

---

## 🔐 **Security Best Practices You Just Learned**

1. **Never commit `.env`** - it's in `.gitignore` ✅
2. **Always commit `.env.example`** - shows what's needed ✅
3. **Different secrets per environment** - dev/staging/production ✅
4. **No hardcoded passwords** - everything in config ✅
5. **Don't print full secrets** - we only print first 30 chars of DB URL ✅

---

## 🔍 **Understanding Pydantic Validation**

**What if someone makes a mistake?**

Try adding this to `.env`:
```
ACCESS_TOKEN_EXPIRE_MINUTES=not-a-number
```

Restart the app - you'll get a clear error:
```
validation error for Settings
ACCESS_TOKEN_EXPIRE_MINUTES
  Input should be a valid integer
```

**Pydantic catches configuration errors BEFORE your app starts!** 🛡️

---

## 🧪 **Try These Experiments**

**Experiment 1:** Add a new setting

Add to `.env`:
```
MAX_LINKS_PER_USER=100
```

Add to `app/config.py`:
```python
# Limits
max_links_per_user: int = 100
```

Use it in `root.py`:
```python
@router.get("/limits")
def get_limits():
    return {"max_links_per_user": settings.max_links_per_user}
```

**Experiment 2:** Required vs Optional

Remove `DATABASE_URL` from `.env` and restart - app won't start!

Add a default value in `config.py`:
```python
database_url: str = "sqlite:///./test.db"  # Now optional
```

**Experiment 3:** Boolean parsing

Try these in `.env` - all work!
```
DEBUG=True
DEBUG=true
DEBUG=1
DEBUG=yes
DEBUG=on
```

---

## 📂 **Your Project Now Looks Like This**

```
shortlink-api/
├── venv/
├── app/
│   ├── __init__.py
│   ├── main.py             ← Uses config!
│   ├── config.py           ← NEW! Settings management
│   ├── routes/
│   │   ├── __init__.py
│   │   └── root.py         ← Uses config!
│   ├── models/
│   │   └── __init__.py
│   └── schemas/
│       └── __init__.py
├── .env                     ← NEW! Your secrets (not in Git)
├── .env.example             ← NEW! Template (in Git)
├── .gitignore              ← Already has .env in it!
├── requirements.txt
```

---

## 🎯 **Phase 3 Complete! 🎉**

**What you have now:**
- ✅ Professional configuration management
- ✅ No hardcoded secrets
- ✅ Type-safe settings with validation
- ✅ Easy to change settings without touching code
- ✅ CORS configured for future frontend
- ✅ Secure by default

**You're now managing configuration like a security-conscious professional!** 🔐

---

## 🔗 **Coming in Phase 4: Docker PostgreSQL**

We'll:
- Install Docker Desktop
- Create `docker-compose.yml`
- Run PostgreSQL in a container
- Connect to it manually (before Python integration)

**Why Docker?** Everyone gets the EXACT same database, no "works on my machine" issues!

---

## 📸 **Before Moving On - Checklist**

- [ ] `.env` file created and app loads it
- [ ] `.env.example` created
- [ ] `python -m app.config` shows your settings
- [ ] App shows config values on startup
- [ ] You understand why we don't commit `.env`
- [ ] You changed a setting in `.env` and saw it reflected in the app

---