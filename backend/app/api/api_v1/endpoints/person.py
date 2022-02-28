from typing import List, Any

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select
from app.core.session import commit_transaction, get_sqlmodel_sesion as get_session
from app.arrangement.models import Person, BusinessHour, Note, ConfirmationReceipt, Audience, OrganizationType, Organization
from app.arrangement.models import TimeLineEvent, Arrangement
from app.arrangement.schemas import ArrangementRead, ArrangementUpdate, ArrangementCreate
from app.arrangement.schemas import PersonRead, PersonCreate, PersonUpdate, PersonReadWithHours, PersonCreateWithNotes, PersonUpdateWithNotes
from app.arrangement.schemas import BusinessHourRead, BusinessHourUpdate, BusinessHourCreate
from app.arrangement.schemas import NoteRead, NoteCreate, NoteUpdate, NoteReadWithAuthors
from app.arrangement.schemas import ConfirmationRecieptRead, ConfirmationRecieptCreate, ConfirmationRecieptUpdate, ConfirmationRecieptWithNoteAndAuthors
from app.arrangement.schemas import AudienceRead, AudienceCreate, AudienceUpdate
from app.arrangement.schemas import OrganizationTypeRead, OrganizationTypeCreate, OrganizationTypeUpdate
from app.arrangement.schemas import OrganizationRead, OrganizationCreate, OrganizationUpdate
from app.arrangement.schemas import TimeLineEventRead, TimeLineEventCreate, TimeLineEventUpdate
from sqlmodel.sql.expression import Select, SelectOfScalar
from app.arrangement.crud import edit_person, edit_note, edit_business_hour, get_persons,get_notes, get_hours
from app.arrangement.crud import get_receipts, edit_receipt, get_audience, edit_audience
from app.arrangement.crud import get_orgtype, edit_orgtype, get_organization, edit_organization
from app.arrangement.crud import get_timeline_event, edit_timeline_event
from app.arrangement.crud import get_arrangement, edit_arrangement


person_router = per = APIRouter()

SelectOfScalar.inherit_cache = True  # type: ignore
Select.inherit_cache = True  # type: ignore


@per.post("/persons/", response_model=PersonRead)
def create_person(*, session: Session = Depends(get_session), person: PersonCreateWithNotes):
    db_notes: List[Note] = [Note.from_orm(note) for note in person.notes if Note.from_orm(note)]
    db_person = Person.from_orm(person)
    db_person.notes.extend(db_notes)
    commit_transaction(session, db_person)
    return db_person


@per.patch("/person/{person_id}", response_model=PersonUpdateWithNotes)
def update_person(*, session: Session = Depends(get_session), person_id: int, person: PersonUpdateWithNotes):
    for note in person.notes:
        edit_note(session, note.id, note)
    for hour in person.businesshours:
        edit_business_hour(session, hour.id, hour)

    db_person = edit_person(session, person_id, person)
    return db_person


@per.get("/person/{person_id}", response_model=PersonReadWithHours)
def read_person(*, session: Session = Depends(get_session), person_id: int):
    person = session.get(Person, person_id)
    print(person)
    if not person:
        raise HTTPException(status_code=404, detail="Person not found")
    return person


@per.get("/persons", response_model=List[PersonRead])
def read_persons(*, session: Session = Depends(get_session), offset: int = 0, limit: int = Query(default=100, lte=100)):
    return get_persons(session, offset, limit)


@per.get("/businesshours", response_model=List[BusinessHourRead])
def read_hours(*, session: Session = Depends(get_session), offset: int = 0, limit: int = Query(default=100, lte=100)):
    return get_hours(session, offset, limit)


@per.get("/businesshour/{businesshour_id}", response_model=BusinessHourRead)
def read_hour(*, session: Session = Depends(get_session), hour_id: int):
    item = session.get(BusinessHour, hour_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@per.post("/businesshours/", response_model=BusinessHourRead)
def create_hours(*, session: Session = Depends(get_session), hour: BusinessHourCreate):
    db_hour = BusinessHour.from_orm(hour)
    commit_transaction(session, db_hour)
    return db_hour


@per.patch("/businesshour/{businesshour_id}", response_model=BusinessHourRead)
def update_hour(*, session: Session = Depends(get_session), hour_id: int, hour: BusinessHourUpdate):
    db_hour = edit_business_hour(session, hour_id, hour)
    return db_hour


@per.post("/notes/", response_model=NoteRead)
def create_note(*, session: Session = Depends(get_session), item: NoteCreate):
    db_item = Note.from_orm(item)
    commit_transaction(session, db_item)
    return db_item


@per.get("/note/{note_id}", response_model=NoteReadWithAuthors)
def read_note(*, session: Session = Depends(get_session), note_id: int):
    item = session.get(Note, note_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@per.get("/notes", response_model=List[NoteRead])
def read_note(*, session: Session = Depends(get_session), offset: int = 0, limit: int = Query(default=100, lte=100)):
    return get_notes(session, offset, limit)


@per.patch("/note/{note_id}", response_model=NoteRead)
def update_note(*, session: Session = Depends(get_session), note_id: int, note: NoteUpdate):
    db_note = edit_note(session, note_id, note)
    return db_note


@per.post("/receipts", response_model=ConfirmationRecieptRead)
def create_receipt(*, session: Session = Depends(get_session), item: ConfirmationRecieptCreate):
    db_item = ConfirmationReceipt.from_orm(item)
    commit_transaction(session, db_item)
    return db_item


@per.get("/receipt/{receipt_id}", response_model=ConfirmationRecieptWithNoteAndAuthors)
def read_receipt(*, session: Session = Depends(get_session), receipt_id: int):
    item = session.get(ConfirmationReceipt, receipt_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@per.get("/receipts", response_model=List[ConfirmationRecieptRead])
def read_receipt(*, session: Session = Depends(get_session), offset: int = 0, limit: int = Query(default=100, lte=100)):
    return get_receipts(session, offset, limit)


@per.patch("/receipt/{receipt_id}", response_model=ConfirmationRecieptRead)
def update_receipt(*, session: Session = Depends(get_session), receipt_id: int, receipt: ConfirmationRecieptUpdate):
    db_receipt = edit_receipt(session, receipt_id, receipt)
    return db_receipt


@per.post("/audiences", response_model=AudienceRead)
def create_audience(*, session: Session = Depends(get_session), item: AudienceCreate):
    db_item = Audience.from_orm(item)
    commit_transaction(session, db_item)
    return db_item


@per.get("/audience/{audience_id}", response_model=AudienceRead)
def read_audience(*, session: Session = Depends(get_session), audience_id: int):
    item = session.get(Audience, audience_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@per.get("/audiences", response_model=List[AudienceRead])
def read_audience(*, session: Session = Depends(get_session), offset: int = 0, limit: int = Query(default=100, lte=100)):
    return get_audience(session, offset, limit)


@per.patch("/audience/{audience_id}", response_model=AudienceRead)
def update_audience(*, session: Session = Depends(get_session), audience_id: int, audience: AudienceUpdate):
    return edit_audience(session, audience_id, audience)


@per.post("/orgtypes", response_model=OrganizationTypeRead)
def create_organization_type(*, session: Session = Depends(get_session), item: OrganizationTypeCreate):
    db_item = OrganizationType.from_orm(item)
    commit_transaction(session, db_item)
    return db_item


@per.get("/orgtypes/{org_type_id}", response_model=OrganizationTypeRead)
def read_organization_type(*, session: Session = Depends(get_session), org_type_id: int):
    item = session.get(OrganizationType, org_type_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@per.get("/orgtypes", response_model=List[OrganizationTypeRead])
def read_organization_types(*, session: Session = Depends(get_session), offset: int = 0, limit: int = Query(default=100, lte=100)):
    return get_orgtype(session, offset, limit)


@per.patch("/orgtypes/{org_type_id}", response_model=OrganizationTypeRead)
def update_organization_type(*, session: Session = Depends(get_session), org_type_id: int, org_type: OrganizationTypeUpdate):
    return edit_orgtype(session, org_type_id, org_type)


@per.post("/organizations", response_model=OrganizationRead)
def create_organization(*, session: Session = Depends(get_session), item: OrganizationCreate):
    db_item = Organization.from_orm(item)
    commit_transaction(session, db_item)
    return db_item


@per.get("/organization/{org_id}", response_model=OrganizationRead)
def read_organization(*, session: Session = Depends(get_session), org_id: int):
    item = session.get(Organization, org_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@per.get("/organizations", response_model=List[OrganizationRead])
def read_organizations(*, session: Session = Depends(get_session), offset: int = 0, limit: int = Query(default=100, lte=100)):
    return get_organization(session, offset, limit)


@per.patch("/organization/{org_id}", response_model=OrganizationRead)
def update_organization(*, session: Session = Depends(get_session), organization_id: int, organization: OrganizationUpdate):
    return edit_organization(session, organization_id, organization)


@per.post("/timelines", response_model=TimeLineEventRead)
def create_timeline(*, session: Session = Depends(get_session), item: TimeLineEventCreate):
    db_item = TimeLineEvent.from_orm(item)
    commit_transaction(session, db_item)
    return db_item


@per.get("/timeline/{timeline_id}", response_model=TimeLineEventRead)
def read_timeline(*, session: Session = Depends(get_session), timeline_id: int):
    item = session.get(TimeLineEvent, timeline_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@per.get("/timelines", response_model=List[TimeLineEventRead])
def read_timelines(*, session: Session = Depends(get_session), offset: int = 0, limit: int = Query(default=100, lte=100)):
    return get_timeline_event(session, offset, limit)


@per.patch("/timeline/{timeline_id}", response_model=TimeLineEventRead)
def update_timeline(*, session: Session = Depends(get_session), timeline_id: int, timeline: TimeLineEventUpdate):
    return edit_timeline_event(session, timeline_id, timeline)


@per.post("/arrangements", response_model=ArrangementRead)
def create_arrangement(*, session: Session = Depends(get_session), item: ArrangementCreate):
    db_item = Arrangement.from_orm(item)
    commit_transaction(session, db_item)
    return db_item


@per.get("/arrangement/{arrangement_id}", response_model=ArrangementRead)
def read_arrangement(*, session: Session = Depends(get_session), arrangement_id: int):
    item = session.get(Arrangement, arrangement_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@per.get("/arrangements", response_model=List[ArrangementRead])
def read_arrangements(*, session: Session = Depends(get_session), offset: int = 0, limit: int = Query(default=100, lte=100)):
    return get_arrangement(session, offset, limit)


@per.patch("/arrangement/{arrangement_id}", response_model=ArrangementRead)
def update_arrangement(*, session: Session = Depends(get_session), arrangement_id: int, arrangement: ArrangementUpdate):
    return edit_arrangement(session,arrangement_id, arrangement)
