from pydantic import BaseModel
from typing import Optional
from .product import Product

class CartProduct(CartProductBase):
    user_id: int
    product_id: int
    product: Product
    quantity: int

    class Config:
        orm_mode = True
