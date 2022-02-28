from fastapi import FastAPI, Depends

from app.core.auth import get_current_active_user
from app.api.api_v1.endpoints.users import users_router
from app.api.api_v1.endpoints.auth import auth_router
from app.api.api_v1.endpoints.location import location_router
from app.api.api_v1.endpoints.base import base_router
from app.api.api_v1.endpoints.person import person_router


def include_routes(app: FastAPI):
    app.include_router(
        users_router,
        prefix="/api/v1",
        tags=["users"],
        dependencies=[Depends(get_current_active_user)],
    )
    app.include_router(auth_router, prefix="/api", tags=["auth"])

    app.include_router(
        location_router,
        prefix="/api/v1",
        tags=["locations"],
        #dependencies=[Depends(get_current_active_user)],
    )

    app.include_router(
        person_router,
        prefix="/api/v1",
        tags=["persons"],
       # dependencies=[Depends(get_current_active_user)],
    )

    app.include_router(
        base_router,
        prefix="/api/v1",
        tags=["home"],
    )
