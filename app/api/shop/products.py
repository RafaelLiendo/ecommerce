from fastapi import APIRouter, Depends
from typing import List

from app.db.session import get_db
from app.core.auth import get_current_active_user, get_current_active_superuser
from app.schemas.product import Product
from app.db.repositories.user_repository import *

users_router = router = APIRouter()


@router.get("/products", response_model=Product)
async def user_me(current_user=Depends(get_current_active_user)):
    return current_user

