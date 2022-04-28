from fastapi import FastAPI, Depends

from app.core.auth import get_current_active_user
from app.api.api_v1.endpoints.users import users_router
from app.api.api_v1.endpoints.auth import auth_router
from app.api.api_v1.endpoints.room import location_router
from app.api.api_v1.endpoints.base import base_router
from app.api.api_v1.endpoints.person import person_router
from app.api.api_v1.endpoints.person import note_router
from app.api.api_v1.endpoints.person import receipt_router
from app.api.api_v1.endpoints.organization import organization_router
from app.api.api_v1.endpoints.organization import hour_router
from app.api.api_v1.endpoints.arrangement import arrangement_router
from app.api.api_v1.endpoints.arrangement import timeline_router
from app.api.api_v1.endpoints.calendar import calendar_router
from app.api.api_v1.endpoints.service import service_router
from app.api.api_v1.endpoints.event import event_router
from app.api.api_v1.endpoints.event import article_router
from app.api.api_v1.endpoints.event import event_service_router
from app.api.api_v1.endpoints.service import requisition_router
from app.api.api_v1.endpoints.html_generator import html_router


def include_routes(app: FastAPI):

    app.include_router(
        person_router,
        prefix="/api/v1",
        tags=["person"],
       # dependencies=[Depends(get_current_active_user)],
    )
    """
    app.include_router(
        note_router,
        prefix="/api/v1",
        tags=["note"],
        # dependencies=[Depends(get_current_active_user)],
    )
    """
    """
    app.include_router(
        receipt_router,
        prefix="/api/v1",
        tags=["confirmation receipt"],
        # dependencies=[Depends(get_current_active_user)],
    )
     """
    app.include_router(
        arrangement_router,
        prefix="/api/v1",
        tags=["arrangement"],
        # dependencies=[Depends(get_current_active_user)],
    )

    app.include_router(
        event_service_router,
        prefix="/api/v1",
        tags=["event service"],
        # dependencies=[Depends(get_current_active_user)],
    )

    app.include_router(
        organization_router,
        prefix="/api/v1",
        tags=["organization & org.type"],
        # dependencies=[Depends(get_current_active_user)],
    )
    """
    app.include_router(
        hour_router,
        prefix="/api/v1",
        tags=["business hours"],
        # dependencies=[Depends(get_current_active_user)],
    )
    """
    app.include_router(
        article_router,
        prefix="/api/v1",
        tags=["article"],
        # dependencies=[Depends(get_current_active_user)],
    )
    """
    app.include_router(
        calendar_router,
        prefix="/api/v1",
        tags=["calendar"],
        # dependencies=[Depends(get_current_active_user)],
    )
    """
    """
    app.include_router(
        service_router,
        prefix="/api/v1",
        tags=["service provider & type"],
        # dependencies=[Depends(get_current_active_user)],
    )
    """
    app.include_router(
        event_router,
        prefix="/api/v1",
        tags=["event"],
        # dependencies=[Depends(get_current_active_user)],
    )

    app.include_router(
        location_router,
        prefix="/api/v1",
        tags=["location & room"],
        # dependencies=[Depends(get_current_active_user)],
    )

    app.include_router(
        timeline_router,
        prefix="/api/v1",
        tags=["timeline"],
        # dependencies=[Depends(get_current_active_user)],
    )
    """
    app.include_router(
        requisition_router,
        prefix="/api/v1",
        tags=["requisition of service"],
        # dependencies=[Depends(get_current_active_user)],
    )
    """
    app.include_router(
        html_router,
        prefix="/api/v1",
        tags=["screen show generator"],
        # dependencies=[Depends(get_current_active_user)],
    )

    app.include_router(
        users_router,
        prefix="/api/v1",
        tags=["user"],
        dependencies=[Depends(get_current_active_user)],
    )
    app.include_router(auth_router, prefix="/api", tags=["auth"])
    """
    app.include_router(
        base_router,
        prefix="/api/v1",
        tags=["home"],
    )
    """

