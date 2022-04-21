from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session
from sqlmodel.sql.expression import Select, SelectOfScalar

from app.core.session import get_sqlmodel_sesion as get_session
from app.arrangement.model.basemodels import Person, Note, ConfirmationReceipt, Audience, OrganizationType, Organization
from app.arrangement.model.basemodels import TimeLineEvent, Arrangement, DisplayLayout, ArrangementType
from app.arrangement.schema.arrangements import ArrangementRead, ArrangementReadExtra, ArrangementUpdate, ArrangementCreate, ArrangementTypeCreate, ArrangementTypeBase
from app.arrangement.schema.arrangements import AudienceRead, AudienceCreate, AudienceUpdate
from app.arrangement.schema.arrangements import TimeLineEventRead, TimeLineEventCreate, TimeLineEventUpdate, TimeLineEventAddOrUpdate
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
def list_audiences(*, session: Session = Depends(get_session), offset: int = 0, limit: int = Query(default=100, lte=100)):
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


@arr.post("/arrangementtype", response_model=ArrangementTypeBase)
def create_arrangement_type(*, session: Session = Depends(get_session), item: ArrangementTypeCreate):
    item = CrudManager(ArrangementType).create_item(session, item)
    return item


@arr.get("/arrangementtype/{arrangement_id}", response_model=ArrangementTypeBase)
def read_arrangement_type(*, session: Session = Depends(get_session), arrangement_id: int):
    item = CrudManager(ArrangementType).read_item(session, arrangement_id)
    return item


@arr.get("/arrangementtype", response_model=List[ArrangementTypeBase])
def read_arrangement_types(*, session: Session = Depends(get_session), offset: int = 0, limit: int = Query(default=100, lte=100)):
    item = CrudManager(ArrangementType).read_items(session, offset, limit)
    return item


@arr.patch("/arrangementtype/{arrangement_id}", response_model=ArrangementTypeBase)
def update_arrangement_type(*, session: Session = Depends(get_session), arrangement_id: int, arrangement: ArrangementTypeBase):
    item = CrudManager(ArrangementType).edit_item(session, arrangement_id, arrangement)
    return item


@arr.delete("/arrangementtype/{arrangement_id}")
def delete_arrangement_type(*, session: Session = Depends(get_session), arrangement_id: int):
    return CrudManager(ArrangementType).delete_item(session, arrangement_id)


@arr.post("/arrangements", response_model=ArrangementRead)
def create_arrangement(*, session: Session = Depends(get_session), item: ArrangementCreate):
    item = CrudManager(Arrangement).create_item(session, item)
    return item


@arr.get("/arrangement/{arrangement_id}", response_model=ArrangementReadExtra)
def read_arrangement(*, session: Session = Depends(get_session), arrangement_id: int):
    item = CrudManager(Arrangement).read_item(session, arrangement_id)
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


@arr.post("/arrangement/{arrangement_id}/note/{note_id}", response_model=ArrangementReadExtra)
def add_arrangement_note(*, session: Session = Depends(get_session), arrangement_id: int, note_id: int):
    db_arrangement = CrudManager(Arrangement).read_item(session, arrangement_id)
    if db_arrangement:
        db_note = CrudManager(Note).read_item(session, note_id)
        if db_note:
            db_arrangement.notes.append(db_note)
        db_arrangement = CrudManager(Arrangement).edit_item(session, arrangement_id, db_arrangement)
    return db_arrangement


@arr.delete("/arrangement/{arrangement_id}/note/{note_id}", response_model=ArrangementReadExtra)
def remove_note_from_arrangement(*, session: Session = Depends(get_session), arrangement_id: int, note_id: int):
    db_arrangement = CrudManager(Arrangement).read_item(session, arrangement_id)
    if db_arrangement:
        for per in db_arrangement.notes:
            if per.id == note_id:
                db_arrangement.notes.remove(per)
                break
        db_arrangement = CrudManager(Arrangement).edit_item(session, arrangement_id, db_arrangement)
    return db_arrangement


@arr.post("/arrangement/{arrangement_id}/timeline/{timeline_id}", response_model=ArrangementReadExtra)
def add_arrangement_timeline_event(*, session: Session = Depends(get_session), arrangement_id: int, timeline_id: int):
    db_arrangement = CrudManager(Arrangement).read_item(session, arrangement_id)
    if db_arrangement:
        db_time = CrudManager(TimeLineEvent).read_item(session, timeline_id)
        if db_time:
            db_arrangement.timeline_events.append(db_time)
        db_arrangement = CrudManager(Arrangement).edit_item(session, arrangement_id, db_arrangement)
    return db_arrangement


@arr.delete("/arrangement/{arrangement_id}/timeline/{timeline_id}", response_model=ArrangementReadExtra)
def remove_timeline_event_from_arrangement(*, session: Session = Depends(get_session), arrangement_id: int, timeline_id: int):
    db_arrangement = CrudManager(Arrangement).read_item(session, arrangement_id)
    if db_arrangement:
        for per in db_arrangement.timeline_events:
            if per.id == timeline_id:
                db_arrangement.timeline_events.remove(per)
                break
        db_arrangement = CrudManager(Arrangement).edit_item(session, arrangement_id, db_arrangement)
    return db_arrangement


@arr.post("/arrangement/{arrangement_id}/planner/{person_id}", response_model=ArrangementReadExtra)
def add_arrangement_planner(*, session: Session = Depends(get_session), arrangement_id: int, person_id: int):
    db_arrangement = CrudManager(Arrangement).read_item(session, arrangement_id)
    if db_arrangement:
        db_person = CrudManager(Person).read_item(session, person_id)
        if db_person:
            db_arrangement.planners.append(db_person)
        db_arrangement = CrudManager(Arrangement).edit_item(session, arrangement_id, db_arrangement)
    return db_arrangement


@arr.delete("/arrangement/{arrangement_id}/planner/{person_id}", response_model=ArrangementReadExtra)
def remove_planner_from_arrangement(*, session: Session = Depends(get_session), arrangement_id: int, person_id: int):
    db_arrangement = CrudManager(Arrangement).read_item(session, arrangement_id)
    if db_arrangement:
        for per in db_arrangement.planners:
            if per.id == person_id:
                db_arrangement.planners.remove(per)
                break
        db_arrangement = CrudManager(Arrangement).edit_item(session, arrangement_id, db_arrangement)
    return db_arrangement


@arr.post("/arrangement/{arrangement_id}/participant/{person_id}", response_model=ArrangementReadExtra)
def add_person_participant_to_arrangement(*, session: Session = Depends(get_session), arrangement_id: int, person_id: int):
    db_arrangement = CrudManager(Arrangement).read_item(session, arrangement_id)
    if db_arrangement:
        db_person = CrudManager(Person).read_item(session, person_id)
        if db_person:
            db_arrangement.people_participants.append(db_person)
        db_arrangement = CrudManager(Arrangement).edit_item(session, arrangement_id, db_arrangement)
    return db_arrangement



@arr.post("/arrangement/{arrangement_id}/display_layout/{layout_id}", response_model=ArrangementReadExtra)
def add_arrangement_display_configuration(*, session: Session = Depends(get_session), arrangement_id: int, layout_id: int):
    db_arrangement = CrudManager(Arrangement).read_item(session, arrangement_id)
    if db_arrangement:
        db_conf = CrudManager(DisplayLayout).read_item(session, layout_id)
        if db_conf:
            db_arrangement.display_layouts.append(db_conf)
        db_arrangement = CrudManager(Arrangement).edit_item(session, arrangement_id, db_arrangement)
    return db_arrangement


@arr.delete("/arrangement/{arrangement_id}/display_layout/{layout_id}", response_model=ArrangementReadExtra)
def remove_arrangement_display_configuration(*, session: Session = Depends(get_session), arrangement_id: int, layout_id: int):
    db_arrangement = CrudManager(Arrangement).read_item(session, arrangement_id)
    if db_arrangement:
        for per in db_arrangement.display_layouts:
            if per.id == layout_id:
                db_arrangement.display_layouts.remove(per)
                break
        db_arrangement = CrudManager(Arrangement).edit_item(session, arrangement_id, db_arrangement)
    return db_arrangement


@arr.delete("/arrangement/{arrangement_id}/participant/{person_id}", response_model=ArrangementReadExtra)
def remove_person_participant_from_arrangement(*, session: Session = Depends(get_session), arrangement_id: int, person_id: int):
    db_arrangement = CrudManager(Arrangement).read_item(session, arrangement_id)
    if db_arrangement:
        for per in db_arrangement.people_participants:
            if per.id == person_id:
                db_arrangement.people_participants.remove(per)
                break
        db_arrangement = CrudManager(Arrangement).edit_item(session, arrangement_id, db_arrangement)
    return db_arrangement


@arr.post("/arrangement/{arrangement_id}/organization/{org_id}", response_model=ArrangementReadExtra)
def add_organization_participant_to_arrangement(*, session: Session = Depends(get_session), arrangement_id: int, org_id: int):
    db_arrangement = CrudManager(Arrangement).read_item(session, arrangement_id)
    if db_arrangement:
        db_org = CrudManager(Organization).read_item(session, org_id)
        if db_org:
            db_arrangement.organization_participants.append(db_org)
        db_arrangement = CrudManager(Arrangement).edit_item(session, arrangement_id, db_arrangement)
    return db_arrangement


@arr.delete("/arrangement/{arrangement_id}/organization/{org_id}", response_model=ArrangementReadExtra)
def remove_organization_participant_from_arrangement(*, session: Session = Depends(get_session), arrangement_id: int, org_id: int):
    db_arrangement = CrudManager(Arrangement).read_item(session, arrangement_id)
    if db_arrangement:
        for per in db_arrangement.organization_participants:
            if per.id == org_id:
                db_arrangement.organization_participants.remove(per)
                break
        db_arrangement = CrudManager(Arrangement).edit_item(session, arrangement_id, db_arrangement)
    return db_arrangement

