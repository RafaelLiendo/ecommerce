from pydantic import BaseModel
from typing import Optional
from pydantic.types import Decimal


class ProductBase(BaseModel):
    name: str
    description: str
    price: Decimal


class ProductOut(ProductBase):
    pass


class ProductCreate(ProductBase):
    class Config:
        orm_mode = True


class ProductEdit(ProductBase):
    class Config:
        orm_mode = True


class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True
