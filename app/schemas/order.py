from pydantic import BaseModel
from typing import List, Optional
import datetime
from pydantic.types import Decimal
from app.db.models import OrderProduct

class Order(OrderBase):
    id: int
    user_id: int
    date: datetime
    total: Decimal
    order_products: List[OrderProduct]

