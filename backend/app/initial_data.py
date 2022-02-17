#!/usr/bin/env python3

from app.users.crud import create_user
from app.users.schemas import UserCreate
from app.core.session import SessionLocal


def init() -> None:
    db = SessionLocal()

    create_user(
        db,
        UserCreate(
            email="admin@webook-fastapi.com",
            password="admin",
            is_active=True,
            is_superuser=True,
        ),
    )


if __name__ == "__main__":
    print("Creating superuser admin@webook-fastapi.com")
    init()
    print("Superuser created")
