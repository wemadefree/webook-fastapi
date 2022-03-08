from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session
from sqlmodel.sql.expression import Select, SelectOfScalar

from app.core.session import get_sqlmodel_sesion as get_session
from app.arrangement.model.basemodels import Person, BusinessHour, Note, ConfirmationReceipt, Audience, OrganizationType, Organization
from app.arrangement.model.basemodels import TimeLineEvent, Arrangement
from app.arrangement.schema.arrangements import ArrangementRead, ArrangementUpdate, ArrangementCreate
from app.arrangement.schema.arrangements import AudienceRead, AudienceCreate, AudienceUpdate
from app.arrangement.schema.arrangements import TimeLineEventRead, TimeLineEventCreate, TimeLineEventUpdate, TimeLineEventAddOrUpdate
from app.arrangement.schema.persons import NoteAddOrUpdate, PersonAddOrUpdate
from app.arrangement.schema.organizations import OrganizationAddOrUpdate
from app.arrangement.factory import CrudManager


arrangement_router = arr = APIRouter()
timeline_router = tim = APIRouter()

SelectOfScalar.inherit_cache = True  # type: ignore
Select.inherit_cache = True  # type: ignore


@arr.post("/audiences", response_model=AudienceRead)
def create_audience(*, session: Session = Depends(get_session), item: AudienceCreate):
    item = CrudManager(Audience).create_item(session, item)
    return item


@arr.get("/audience/{audience_id}", response_model=AudienceRead)
def read_audience(*, session: Session = Depends(get_session), audience_id: int):
    item = CrudManager(Audience).read_item(session, audience_id)
    return item


@arr.get("/audiences", response_model=List[AudienceRead])
def read_audience(*, session: Session = Depends(get_session), offset: int = 0, limit: int = Query(default=100, lte=100)):
    item = CrudManager(Audience).read_items(session, offset, limit)
    return item


@arr.patch("/audience/{audience_id}", response_model=AudienceRead)
def update_audience(*, session: Session = Depends(get_session), audience_id: int, audience: AudienceUpdate):
    item = CrudManager(Audience).edit_item(session, audience_id, audience)
    return item


@arr.delete("/audience/{audience_id}")
def delete_audience(*, session: Session = Depends(get_session), audience_id: int):
    return CrudManager(Audience).delete_item(session, audience_id)


@tim.post("/timelines", response_model=TimeLineEventRead)
def create_timeline(*, session: Session = Depends(get_session), item: TimeLineEventCreate):
    item = CrudManager(TimeLineEvent).create_item(session, item)
    return item


@tim.get("/timeline/{timeline_id}", response_model=TimeLineEventRead)
def read_timeline(*, session: Session = Depends(get_session), timeline_id: int):
    item = CrudManager(TimeLineEvent).read_item(session, timeline_id)
    return item


@tim.get("/timelines", response_model=List[TimeLineEventRead])
def read_timelines(*, session: Session = Depends(get_session), offset: int = 0, limit: int = Query(default=100, lte=100)):
    item = CrudManager(TimeLineEvent).read_items(session, offset, limit)
    return item


@tim.patch("/timeline/{timeline_id}", response_model=TimeLineEventRead)
def update_timeline(*, session: Session = Depends(get_session), timeline_id: int, timeline: TimeLineEventUpdate):
    item = CrudManager(TimeLineEvent).edit_item(session, timeline_id, timeline)
    return item


@tim.delete("/timeline/{timeline_id}")
def delete_timeline(*, session: Session = Depends(get_session), timeline_id: int):
    return CrudManager(TimeLineEvent).delete_item(session, timeline_id)


@arr.post("/arrangements", response_model=ArrangementRead)
def create_arrangement(*, session: Session = Depends(get_session), item: ArrangementCreate):
    item = CrudManager(Arrangement).create_item(session, item)
    return item


@arr.get("/arrangement/{arrangement_id}", response_model=ArrangementRead)
def read_arrangement(*, session: Session = Depends(get_session), arrangement_id: int):
    item = CrudManager(Arrangement).create_item(session, arrangement_id)
    return item


@arr.get("/arrangements", response_model=List[ArrangementRead])
def read_arrangements(*, session: Session = Depends(get_session), offset: int = 0, limit: int = Query(default=100, lte=100)):
    item = CrudManager(Arrangement).read_items(session, offset, limit)
    return item


@arr.patch("/arrangement/{arrangement_id}", response_model=ArrangementRead)
def update_arrangement(*, session: Session = Depends(get_session), arrangement_id: int, arrangement: ArrangementUpdate):
    item = CrudManager(Arrangement).edit_item(session, arrangement_id, arrangement)
    return item


@arr.delete("/arrangement/{arrangement_id}")
def delete_arrangement(*, session: Session = Depends(get_session), arrangement_id: int):
    return CrudManager(Arrangement).delete_item(session, arrangement_id)


@arr.post("/arrangement/{arrangement_id}/addtimeline", response_model=ArrangementRead)
def add_timeline(*, session: Session = Depends(get_session), arrangement_id: int, timeline: TimeLineEventAddOrUpdate):
    db_arrangement = CrudManager(Arrangement).read_item(session, arrangement_id)
    if db_arrangement:
        db_timeline = CrudManager(TimeLineEvent).edit_item(session, timeline.id, timeline)
        if db_timeline:
            db_arrangement.timeline_events.append(db_timeline)
    db_arrangement = CrudManager(Arrangement).edit_item(session, arrangement_id, db_arrangement)
    return db_arrangement


@arr.post("/arrangement/{arrangement_id}/addnote", response_model=ArrangementRead)
def add_note(*, session: Session = Depends(get_session), arrangement_id: int, note: NoteAddOrUpdate):
    db_arrangement = CrudManager(Arrangement).read_item(session, arrangement_id)
    if db_arrangement:
        db_note = CrudManager(Note).edit_item(session, note.id, note)
        if db_note:
            db_arrangement.notes.append(db_note)
    db_arrangement = CrudManager(Arrangement).edit_item(session, arrangement_id, db_arrangement)
    return db_arrangement


@arr.post("/arrangement/{arrangement_id}/addplanner", response_model=ArrangementRead)
def add_planner(*, session: Session = Depends(get_session), arrangement_id: int, person: PersonAddOrUpdate):
    db_arrangement = CrudManager(Arrangement).read_item(session, arrangement_id)
    if db_arrangement:
        db_person = CrudManager(Person).edit_item(session, person.id, person)
        if db_person:
            db_arrangement.planners.append(db_person)
    db_arrangement = CrudManager(Arrangement).edit_item(session, arrangement_id, db_arrangement)
    return db_arrangement


@arr.post("/arrangement/{arrangement_id}/addpeople_participants", response_model=ArrangementRead)
def add_people_participants(*, session: Session = Depends(get_session), arrangement_id: int, person: PersonAddOrUpdate):
    db_arrangement = CrudManager(Arrangement).read_item(session, arrangement_id)
    if db_arrangement:
        db_person = CrudManager(Person).edit_item(session, person.id, person)
        if db_person:
            db_arrangement.people_participants.append(db_person)
    db_arrangement = CrudManager(Arrangement).edit_item(session, arrangement_id, db_arrangement)
    return db_arrangement


@arr.post("/arrangement/{arrangement_id}/addorganization_participants", response_model=ArrangementRead)
def add_organization_participants(*, session: Session = Depends(get_session), arrangement_id: int, organization: OrganizationAddOrUpdate):
    db_arrangement = CrudManager(Arrangement).read_item(session, arrangement_id)
    if db_arrangement:
        db_org = CrudManager(Organization).edit_item(session, organization.id, organization)
        if db_org:
            db_arrangement.organization_participants.append(db_org)
    db_arrangement = CrudManager(Arrangement).edit_item(session, arrangement_id, db_arrangement)
    return db_arrangement

