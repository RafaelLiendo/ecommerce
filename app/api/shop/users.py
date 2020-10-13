from fastapi import APIRouter, Depends
from typing import List

from app.db.session import get_db
from app.core.auth import get_current_active_user, get_current_active_superuser
from app.schemas.user import User, UserCreate, UserEdit
from app.db.repositories.user_repository import *

users_router = router = APIRouter()


@router.get("/me", response_model=User)
async def user_me(current_user=Depends(get_current_active_user)):
    return current_user

