from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session
from sqlmodel.sql.expression import Select, SelectOfScalar

from app.core.session import get_sqlmodel_sesion as get_session
from app.arrangement.model.basemodels import Person, BusinessHour, Note, ConfirmationReceipt, Audience, OrganizationType, Organization
from app.arrangement.model.basemodels import TimeLineEvent, Arrangement
from app.arrangement.schema.arrangements import ArrangementRead, ArrangementUpdate, ArrangementCreate
from app.arrangement.schema.arrangements import AudienceRead, AudienceCreate, AudienceUpdate
from app.arrangement.schema.arrangements import TimeLineEventRead, TimeLineEventCreate, TimeLineEventUpdate
from app.arrangement.factory import CrudManager


arrangement_router = arr = APIRouter()

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


@arr.post("/timelines", response_model=TimeLineEventRead)
def create_timeline(*, session: Session = Depends(get_session), item: TimeLineEventCreate):
    item = CrudManager(TimeLineEvent).create_item(session, item)
    return item


@arr.get("/timeline/{timeline_id}", response_model=TimeLineEventRead)
def read_timeline(*, session: Session = Depends(get_session), timeline_id: int):
    item = CrudManager(TimeLineEvent).read_item(session, timeline_id)
    return item


@arr.get("/timelines", response_model=List[TimeLineEventRead])
def read_timelines(*, session: Session = Depends(get_session), offset: int = 0, limit: int = Query(default=100, lte=100)):
    item = CrudManager(TimeLineEvent).read_items(session, offset, limit)
    return item


@arr.patch("/timeline/{timeline_id}", response_model=TimeLineEventRead)
def update_timeline(*, session: Session = Depends(get_session), timeline_id: int, timeline: TimeLineEventUpdate):
    item = CrudManager(TimeLineEvent).edit_item(session, timeline_id, timeline)
    return item


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