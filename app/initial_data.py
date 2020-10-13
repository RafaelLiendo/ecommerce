#!/usr/bin/env python3

from app.db.session import get_db
from app.db.crud import create_user, get_user_by_email
from app.db.schemas import UserCreate
from app.db.session import SessionLocal


def init() -> None:
    db = SessionLocal()
    admin_user_exists = get_user_by_email(db, "admin@ecommerce.com")
    if not admin_user_exists:
        create_user(
            db,
            UserCreate(
                email="admin@ecommerce.com",
                password="password",
                is_active=True,
                is_superuser=True,
            ),
        )


if __name__ == "__main__":
    print("Creating superuser admin@ecommerce.com")
    init()
    print("Superuser created")
