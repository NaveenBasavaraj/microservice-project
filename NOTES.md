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


