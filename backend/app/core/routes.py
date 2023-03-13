from app.api.api_v1.endpoints.arrangement import arrangement_router, audience_router
from app.api.api_v1.endpoints.auth import auth_router
from app.api.api_v1.endpoints.base import base_router
from app.api.api_v1.endpoints.event import article_router, event_router
from app.api.api_v1.endpoints.html_generator import html_router
from app.api.api_v1.endpoints.organization import organization_router
from app.api.api_v1.endpoints.outlook_events import outlook_router
from app.api.api_v1.endpoints.person import person_router
from app.api.api_v1.endpoints.room import location_router
from app.api.api_v1.endpoints.users import users_router
from app.users.auth import get_current_active_user
from app.webapp.login_route import login_router
from fastapi import Depends, FastAPI


def include_routes(app: FastAPI):

    app.include_router(
        person_router,
        prefix="/api/v1",
        tags=["person"],
        dependencies=[Depends(get_current_active_user)],
    )

    app.include_router(
        arrangement_router,
        prefix="/api/v1",
        tags=["arrangement"],
        dependencies=[Depends(get_current_active_user)],
    )

    app.include_router(
        audience_router,
        prefix="/api/v1",
        tags=["audience"],
        dependencies=[Depends(get_current_active_user)],
    )

    app.include_router(
        organization_router,
        prefix="/api/v1",
        tags=["organization & org.type"],
        dependencies=[Depends(get_current_active_user)],
    )

    app.include_router(
        article_router,
        prefix="/api/v1",
        tags=["article"],
        dependencies=[Depends(get_current_active_user)],
    )

    app.include_router(
        event_router,
        prefix="/api/v1",
        tags=["event"],
        dependencies=[Depends(get_current_active_user)],
    )

    app.include_router(
        location_router,
        prefix="/api/v1",
        tags=["location & room"],
        dependencies=[Depends(get_current_active_user)],
    )

    app.include_router(
        html_router,
        prefix="/api/v1",
        tags=["screen show generator"],
        dependencies=[Depends(get_current_active_user)],
    )

    app.include_router(
        users_router,
        prefix="/api/v1",
        tags=["user"],
        dependencies=[Depends(get_current_active_user)],
    )
    app.include_router(auth_router, prefix="/api", tags=["auth"])

    app.include_router(login_router, prefix="/api", tags=["auth-webapp"])  # new

    app.include_router(
        outlook_router,
        prefix="/api/v1",
        tags=["user"],
        dependencies=[Depends(get_current_active_user)],
    )

    """
    app.include_router(
        base_router,
        prefix="",
        tags=["home"],
    )
    """
