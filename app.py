# app.py
from fastapi import FastAPI
from main import run_bot

app = FastAPI()

@app.get("/")
def root():
    return {"status": "Guardian AI Trader API is running."}

@app.get("/run-trader")
def run_trader():
    result = run_bot()
    return result
