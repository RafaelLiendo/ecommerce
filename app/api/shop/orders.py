from fastapi import APIRouter, Depends
from typing import List

from app.schemas.product import Product
from app.schemas.order import Order

users_router = router = APIRouter()


@router.get("/orders", response_model=List[Order])
async def get_orders(
    db=Depends(get_db),
    skip: int = 0,
    limit: int = 100
):
    pass


@router.post("/orders", response_model=List[Order])
async def create_order(
    db=Depends(get_db),
    current_user=Depends(get_current_active_superuser)
):
    pass
