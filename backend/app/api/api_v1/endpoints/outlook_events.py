from datetime import datetime
from typing import List

import httpx
from app.core.session import get_session
from app.graph.client.graph import GraphClient
from app.graph.graph_client_fab import create_graph_client
from app.users.auth import get_current_active_superuser, get_current_active_user
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

outlook_router = outlook = APIRouter()


@outlook.get("/outlook/{user_object_id}")
def get_outlook_events_for_user(
    user_object_id: str,
    start_datetime_iso_8601: str,
    end_datetime_iso_8601: str,
    current_user=Depends(get_current_active_superuser),
):
    graph_client: GraphClient = create_graph_client()

    if graph_client is None:
        return None

    response: httpx.Response = graph_client.exhaust(
        url=f"https://graph.microsoft.com/v1.0/users/{user_object_id}/calendar/calendarView?StartDateTime={start_datetime_iso_8601}&EndDateTime={end_datetime_iso_8601}"
    )

    return response.json()
