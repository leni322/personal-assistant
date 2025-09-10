from fastapi import FastAPI
from app.api import habits_API, products_API

app = FastAPI()

app.include_router(habits_API.router, prefix="/api", tags=["habits"])
app.include_router(products_API.router, prefix="/api", tags=["products"])

@app.get("/")
def read_root():
    return {"message": "Привет! FastAPI работает 🚀"}
