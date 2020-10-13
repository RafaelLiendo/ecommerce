from fastapi import APIRouter, Depends
from typing import List

from app.db.session import get_db
from app.core.auth import get_current_active_user, get_current_active_superuser
from app.schemas.user import User, UserCreate, UserEdit
from app.db.repositories.user_repository import *

users_router = router = APIRouter()


@router.get("/", response_model=List[User])
async def users_list(
    db=Depends(get_db),
    current_user=Depends(get_current_active_superuser),
    skip: int = 0,
    limit: int = 100,
):
    users = get_users(db, skip=skip, limit=limit)
    return users


@router.get("/me", response_model=User)
async def user_me(current_user=Depends(get_current_active_user)):
    return current_user


@router.get("/{user_id}", response_model=User)
async def user_details(
    user_id: int,
    db=Depends(get_db),
    current_user=Depends(get_current_active_superuser),
):
    user = get_user(db, user_id)
    return user


@router.post("/", response_model=User)
async def user_create(
    user: UserCreate,
    db=Depends(get_db),
    current_user=Depends(get_current_active_superuser),
):
    return create_user(db, user)


@router.put("/{user_id}", response_model=User)
async def user_edit(
    user_id: int,
    user: UserEdit,
    db=Depends(get_db),
    current_user=Depends(get_current_active_superuser),
):
    return edit_user(db, user_id, user)


@router.delete("/{user_id}", response_model=User)
async def user_delete(
    user_id: int,
    db=Depends(get_db),
    current_user=Depends(get_current_active_superuser),
):
    return delete_user(db, user_id)
