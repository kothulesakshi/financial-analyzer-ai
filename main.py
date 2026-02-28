

from fastapi import FastAPI
import uvicorn

# Create FastAPI app
app = FastAPI(
    title="My API",
    description="Simple FastAPI project",
    version="1.0"
)

# Home route
@app.get("/")
def home():
    return {"message": "API is running successfully 🚀"}

# Test route
@app.get("/test")
def test():
    return {"status": "working"}

# Health check route
@app.get("/health")
def health():
    return {"health": "ok"}

# Run server (optional - only for direct run)
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)