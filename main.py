from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Server is running"}

@app.get("/info")
def get_info():
    today = datetime.now()
    new_year = datetime(year=today.year + 1, month=1, day=1)
    days_left = (new_year - today).days

    return {
        "days_before_new_year": days_left
    }