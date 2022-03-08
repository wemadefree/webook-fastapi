from typing import List

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session
from app.core.session import get_sqlmodel_sesion as get_session
from app.arrangement.model.basemodels import Calendar, Room, Person
from app.arrangement.schema.calendar import CalendarRead, CalendarReadExtra, CalendarCreate, CalendarUpdate
from app.arrangement.schema.rooms import RoomAddOrUpdate
from app.arrangement.schema.persons import PersonAddOrUpdate
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


@cal.delete("/calendar/{calendar_id}")
def delete_calendar(*, session: Session = Depends(get_session), calendar_id: int):
    return CrudManager(Calendar).delete_item(session, calendar_id)


@cal.post("/calendar/{calendar_id}/addroom", response_model=CalendarReadExtra)
def add_room(*, session: Session = Depends(get_session), calendar_id: int, room: RoomAddOrUpdate):
    db_cal = CrudManager(Calendar).read_item(session, calendar_id)
    if db_cal:
        db_room = CrudManager(Room).edit_item(session, room.id, room)
        if db_room:
            db_cal.room_resources.append(db_room)
    db_cal = CrudManager(Calendar).edit_item(session, calendar_id, db_cal)
    return db_cal


@cal.post("/calendar/{calendar_id}/addperson", response_model=CalendarReadExtra)
def add_room(*, session: Session = Depends(get_session), calendar_id: int, person: PersonAddOrUpdate):
    db_cal = CrudManager(Calendar).read_item(session, calendar_id)
    if db_cal:
        db_person = CrudManager(Person).edit_item(session, person.id, person)
        if db_person:
            db_cal.people_resources.append(db_person)
    db_cal = CrudManager(Calendar).edit_item(session, calendar_id, db_cal)
    return db_cal
