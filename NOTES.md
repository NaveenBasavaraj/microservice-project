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
