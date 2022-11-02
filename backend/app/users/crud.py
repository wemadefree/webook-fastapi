from typing import List, Optional

from app.core.security import get_password_hash
from app.users import models, schemas
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.sql import text


def get_user(db: Session, user_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


def get_user_by_email(db: Session, email: str) -> schemas.UserBase:
    usr = db.query(models.User).filter(models.User.email == email).first()
    return usr


def get_users(db: Session, skip: int = 0, limit: int = 100) -> List[schemas.UserOut]:
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        is_active=user.is_active,
        is_superuser=user.is_superuser,
        hashed_password=hashed_password,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int):
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="User not found")

    # also remove the email addresses associated with this user, if any
    db.execute(
        text("DELETE FROM account_emailaddress WHERE user_id = :uid"),
        params={"uid": user_id},
    )
    db.execute(
        text("DELETE FROM socialaccount_socialaccount WHERE user_id = :uid"),
        params={"uid": user_id},
    )
    db.execute(
        text("DELETE FROM users_user_groups WHERE user_id = :uid"),
        params={"uid": user_id},
    )

    db.delete(user)
    db.commit()
    return user


def edit_user(db: Session, user_id: int, user: schemas.UserEdit) -> schemas.User:
    db_user = get_user(db, user_id)
    if not db_user:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="User not found")
    update_data = user.dict(exclude_unset=True)

    if "password" in update_data:
        update_data["hashed_password"] = get_password_hash(user.password)
        del update_data["password"]

    for key, value in update_data.items():
        setattr(db_user, key, value)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
