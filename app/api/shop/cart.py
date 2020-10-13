from fastapi import APIRouter, Depends
from typing import List

from app.schemas.product import Product
from app.schemas.cart_product import CartProduct

users_router = router = APIRouter()


@router.get("/cart", response_model=List[CartProduct])
async def get_cart_products(db=Depends(get_db)):
    pass


@router.post("/cart", response_model=List[CartProduct])
async def create_cart_product():
    pass


@router.delete("/cart", response_model=List[CartProduct])
async def delete_cart_product(db=Depends(get_db)):
    pass
