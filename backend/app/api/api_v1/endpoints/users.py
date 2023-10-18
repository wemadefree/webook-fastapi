from typing import List

from app.core.session import get_session
from app.users.auth import get_current_active_superuser, get_current_active_user
from app.users.crud import (
    create_user,
    delete_user,
    edit_user,
    get_user,
    get_users,
    reactivate_user,
)
from app.users.schemas import User, UserCreate, UserEdit, UserOut
from fastapi import APIRouter, Depends, Request, Response

users_router = r = APIRouter()


@r.get("/users", response_model=List[User], response_model_exclude_none=True)
async def users_list(
    response: Response,
    db=Depends(get_session),
    current_user=Depends(get_current_active_superuser),
):
    """
    Get all users
    """
    users = get_users(db)
    # This is necessary for react-admin to work
    response.headers["Content-Range"] = f"0-9/{len(users)}"
    return users


@r.get("/users/me", response_model=User, response_model_exclude_none=True)
async def user_me(current_user=Depends(get_current_active_user)):
    """
    Get own user
    """
    return current_user


@r.get(
    "/users/{user_id}",
    response_model=User,
    response_model_exclude_none=True,
)
async def user_details(
    request: Request,
    user_id: int,
    db=Depends(get_session),
    current_user=Depends(get_current_active_superuser),
):
    """
    Get any user details
    """
    user = get_user(db, user_id)
    return user


@r.post("/users", response_model=User, response_model_exclude_none=True)
async def user_create(
    request: Request,
    user: UserCreate,
    db=Depends(get_session),
    current_user=Depends(get_current_active_superuser),
):
    """
    Create a new user
    """
    return create_user(db, user)


@r.put("/users/{user_id}", response_model=User, response_model_exclude_none=True)
async def user_edit(
    request: Request,
    user_id: int,
    user: UserEdit,
    db=Depends(get_session),
    current_user=Depends(get_current_active_superuser),
):
    """
    Update existing user
    """
    return edit_user(db, user_id, user)


@r.delete("/users/{user_id}", response_model=User, response_model_exclude_none=True)
async def user_delete(
    request: Request,
    user_id: int,
    db=Depends(get_session),
    current_user=Depends(get_current_active_superuser),
):
    """
    Delete existing user
    """
    return delete_user(db, user_id)


@r.patch("/users/{user_id}", response_model=User, response_model_exclude_none=True)
async def user_reactivate(
    request: Request,
    user_id: int,
    db=Depends(get_session),
    current_user=Depends(get_current_active_superuser),
):
    """
    Reactivate a deactivated user
    """
    return reactivate_user(db, user_id)
