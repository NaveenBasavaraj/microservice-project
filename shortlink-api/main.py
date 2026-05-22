from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message":"Hello World! 🚀"}

@app.get("/health")
def health_checks():
    return {
            "status":"healthy", 
            "service": "ShortLink API"
            }