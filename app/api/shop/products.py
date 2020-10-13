from fastapi import APIRouter, Depends
from typing import List

from app.schemas.product import Product

users_router = router = APIRouter()


@router.get("/products", response_model=List[Product])
async def get_products(
    db=Depends(get_db),
    skip: int = 0,
    limit: int = 100
):
    pass

