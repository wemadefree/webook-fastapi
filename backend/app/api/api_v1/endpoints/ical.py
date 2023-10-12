import time
from typing import List

from app.arrangement.model.basemodels import Event, Person
from app.core.ical import create_calendar
from app.core.session import get_session
from fastapi import APIRouter, Depends, HTTPException, Query, Response
from sqlalchemy.orm import Session

ical_router = ical = APIRouter()


@ical.get("/ical/directly_responsible/{person_id}")
def get_ical(*, session: Session = Depends(get_session), person_id: int):
    """
    Get all events that a person is directly responsible for in iCal format
    """

    person = session.query(Person).filter(Person.id == person_id).first()

    if person is None:
        raise HTTPException(status_code=404, detail="Person not found")

    calendar = create_calendar(session, person.responsible_for_events)
    return Response(content=calendar, media_type="text/calendar")
