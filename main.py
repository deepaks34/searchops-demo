from fastapi import FastAPI
from datetime import datetime
import os

app = FastAPI()

@app.get("/health")
def health():
    return {
        "status": "ok",
        "env": os.getenv("ENVIRONMENT", "dev"),
        "build": os.getenv("BUILD_VERSION", "local"),
        "time": datetime.utcnow()
    }

@app.get("/search")
def search(q: str):
    return {
        "query": q,
        "result": f"result for {q}",
        "build": os.getenv("BUILD_VERSION", "local")
    }

