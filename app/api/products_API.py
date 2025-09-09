from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import date
from app import models
from app.db import SessionLocal, engine
from app.schemas.product_sh import Product, ProductCreate, ProductUpdate, ProductBase

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Создать продукт
@router.post("/products/", response_model=Product)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

# Получить все продукты
@router.get("/products/", response_model=list[Product])
def read_products(db: Session = Depends(get_db)):
    return db.query(models.Product).all()

# Получить только просроченные продукты
@router.get("/products/expired/", response_model=list[Product])
def read_expired_products(db: Session = Depends(get_db)):
    today = date.today()
    return db.query(models.Product).filter(models.Product.expiration_date < today).all()

# Обновить продукт
@router.put("/products/{product_id}", response_model=schemas.Product)
def update_product(product_id: int, product: ProductUpdate, db: Session = Depends(get_db)):
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")

    for key, value in product.dict(exclude_unset=True).items():
        setattr(db_product, key, value)

    db.commit()
    db.refresh(db_product)
    return db_product

# Удалить продукт
@router.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")

    db.delete(db_product)
    db.commit()
    return {"message": "Product deleted"}
