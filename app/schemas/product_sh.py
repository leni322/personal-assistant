from pydantic import BaseModel
from datetime import date

class ProductBase(BaseModel):
    name: str
    purchase_date: date
    expiration_date: date

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: str | None = None
    purchase_date: date | None = None
    expiration_date: date | None = None

class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True
