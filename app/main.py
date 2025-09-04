from fastapi import FastAPI
from app.api import habits

app = FastAPI()

app.include_router(habits.router, prefix="/api", tags=["Habits"])

@app.get("/")
def read_root():
    return {"message": "Привет! FastAPI работает 🚀"}
