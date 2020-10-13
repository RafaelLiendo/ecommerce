from pydantic import BaseModel
from typing import List, Optional
import datetime
from pydantic.types import Decimal
from app.db.models import OrderProduct
from .product import Product


class OrderProduct(OrderProductBase):
    order_id: int
    product_id: int
    product: Product
    quantity: int
    subtotal: Decimal

    class Config:
        orm_mode = True
