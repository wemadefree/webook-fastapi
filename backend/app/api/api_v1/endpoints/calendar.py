from typing import List

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session
from app.core.session import get_sqlmodel_sesion as get_session
from app.arrangement.model.basemodels import Calendar
from app.arrangement.schema.calendar import CalendarRead, CalendarReadExtra, CalendarCreate, CalendarUpdate
from app.arrangement.factory import CrudManager

calendar_router = cal = APIRouter()


@cal.post("/calendars", response_model=CalendarRead)
def create_calendar(*, session: Session = Depends(get_session), calendar: CalendarCreate):
    calendar_item = CrudManager(Calendar).create_item(session, calendar)
    return calendar_item


@cal.get("/calendars", response_model=List[CalendarRead])
def read_calendars(*, session: Session = Depends(get_session), offset: int = 0, limit: int = Query(default=100, lte=100)):
    locations = CrudManager(Calendar).read_items(session, offset, limit)
    return locations


@cal.get("/calendar/{calendar_id}", response_model=CalendarReadExtra)
def read_calendar(*, session: Session = Depends(get_session), calendar_id: int):
    calendar_item = CrudManager(Calendar).read_item(session, calendar_id)
    return calendar_item


@cal.patch("/calendar/{calendar_id}", response_model=CalendarRead)
def update_calendar(*, session: Session = Depends(get_session), calendar_id: int, calendar: CalendarUpdate):
    calendar_item = CrudManager(Calendar).edit_item(session, calendar_id, calendar)
    return calendar_item