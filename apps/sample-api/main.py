from fastapi import FastAPI
import os
import time

app = FastAPI()

@app.get("/healthz")
def healthz():
    return {"status": "ok"}

@app.get("/")
def root():
    return {
        "service": "sample-api",
        "env": os.getenv("ENV", "dev"),
        "time": int(time.time())
    }