from sqlalchemy import Column, String, Date, Integer
from app.db import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    purchase_date = Column(Date, nullable=False)
    expiration_date = Column(Date, nullable=False)
