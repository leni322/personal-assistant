from fastapi import FastAPI
from app.api import habits_API, products_API

app = FastAPI()

app.include_router(habits_API.router, prefix="/api", tags=["habits"])

@app.get("/")
def read_root():
    return {"message": "Привет! FastAPI работает 🚀"}
