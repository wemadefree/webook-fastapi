from typing import List
from fastapi import APIRouter, Depends, Query
from sqlmodel import Session
from sqlmodel.sql.expression import Select, SelectOfScalar

from app.core.session import get_sqlmodel_sesion as get_session
from app.arrangement.model.basemodels import Person, BusinessHour, Note, ConfirmationReceipt, Audience, OrganizationType, Organization
from app.arrangement.schema.persons import PersonRead, PersonReadExtra, PersonCreate, PersonUpdate, PersonReadWithHours, PersonCreateWithNotes, PersonUpdateWithNotes
from app.arrangement.schema.persons import NoteRead, NoteCreate, NoteUpdate, NoteAddOrUpdate, NoteReadWithAuthors
from app.arrangement.schema.persons import ConfirmationRecieptRead, ConfirmationRecieptCreate, ConfirmationRecieptUpdate, ConfirmationRecieptWithNoteAndAuthors
from app.arrangement.schema.bussineshours import BusinessHourAddOrUpdate
from app.arrangement.factory import CrudManager


person_router = per = APIRouter()
note_router = nt = APIRouter()

SelectOfScalar.inherit_cache = True  # type: ignore
Select.inherit_cache = True  # type: ignore


@per.post("/persons/", response_model=PersonRead)
def create_person(*, session: Session = Depends(get_session), person: PersonCreateWithNotes):
    db_notes: List[Note] = [Note.from_orm(note) for note in person.notes if Note.from_orm(note)]
    db_person = Person.from_orm(person)
    db_person.notes.extend(db_notes)
    db_person = CrudManager(Person).create_item(session, db_person)
    return db_person


@per.patch("/person/{person_id}", response_model=PersonReadExtra)
def update_person(*, session: Session = Depends(get_session), person_id: int, person: PersonUpdateWithNotes):
    if person.notes:
        for note in person.notes:
            CrudManager(Note).edit_item(session, note.id, note)
    if person.businesshours:
        for hour in person.businesshours:
            CrudManager(BusinessHour).edit_item(session, hour.id, hour)

    db_person = CrudManager(Person).edit_item(session, person_id, person)
    return db_person


@per.post("/person/{person_id}/addnote", response_model=PersonReadExtra)
def add_note(*, session: Session = Depends(get_session), person_id: int, note: NoteAddOrUpdate):
    db_person = CrudManager(Person).read_item(session, person_id)
    if db_person:
        db_note = CrudManager(Note).edit_item(session, note.id, note)
        if db_note:
            db_person.notes.append(db_note)
    db_person = CrudManager(Person).edit_item(session, person_id, db_person)
    return db_person


@per.post("/person/{person_id}/addbusinesshour", response_model=PersonReadExtra)
def add_hours(*, session: Session = Depends(get_session), person_id: int, hour: BusinessHourAddOrUpdate):
    db_person = CrudManager(Person).read_item(session, person_id)
    if db_person:
        db_hour = CrudManager(BusinessHour).edit_item(session, hour.id, hour)
        if db_hour:
            db_person.businesshours.append(db_hour)
    db_person = CrudManager(Person).edit_item(session, person_id, db_person)
    return db_person


@per.get("/person/{person_id}", response_model=PersonReadExtra)
def read_person(*, session: Session = Depends(get_session), person_id: int):
    item = CrudManager(Person).read_item(session, person_id)
    return item


@per.get("/persons", response_model=List[PersonRead])
def read_persons(*, session: Session = Depends(get_session), offset: int = 0, limit: int = Query(default=100, lte=100)):
    item = CrudManager(Person).read_items(session, offset, limit)
    return item


@per.delete("/person/{person_id}")
def delete_person(*, session: Session = Depends(get_session), person_id: int):
    return CrudManager(Person).delete_item(session, person_id)


@nt.post("/notes/", response_model=NoteRead)
def create_note(*, session: Session = Depends(get_session), item: NoteCreate):
    item = CrudManager(Note).create_item(session, item)
    return item


@nt.get("/note/{note_id}", response_model=NoteReadWithAuthors)
def read_note(*, session: Session = Depends(get_session), note_id: int):
    item = CrudManager(Note).read_item(session, note_id)
    return item


@nt.get("/notes", response_model=List[NoteRead])
def read_note(*, session: Session = Depends(get_session), offset: int = 0, limit: int = Query(default=100, lte=100)):
    item = CrudManager(Note).read_items(session, offset, limit)
    return item


@nt.patch("/note/{note_id}", response_model=NoteRead)
def update_note(*, session: Session = Depends(get_session), note_id: int, note: NoteUpdate):
    item = CrudManager(Note).edit_item(session, note_id, note)
    return item


@nt.delete("/note/{note_id}")
def delete_note(*, session: Session = Depends(get_session), note_id: int):
    return CrudManager(Note).delete_item(session, note_id)


@per.post("/receipts", response_model=ConfirmationRecieptRead)
def create_receipt(*, session: Session = Depends(get_session), item: ConfirmationRecieptCreate):
    item = CrudManager(ConfirmationReceipt).create_item(session, item)
    return item


@per.get("/receipt/{receipt_id}", response_model=ConfirmationRecieptWithNoteAndAuthors)
def read_receipt(*, session: Session = Depends(get_session), receipt_id: int):
    item = CrudManager(ConfirmationReceipt).read_item(session, receipt_id)
    return item


@per.get("/receipts", response_model=List[ConfirmationRecieptRead])
def read_receipt(*, session: Session = Depends(get_session), offset: int = 0, limit: int = Query(default=100, lte=100)):
    item = CrudManager(ConfirmationReceipt).read_items(session, offset, limit)
    return item


@per.patch("/receipt/{receipt_id}", response_model=ConfirmationRecieptRead)
def update_receipt(*, session: Session = Depends(get_session), receipt_id: int, receipt: ConfirmationRecieptUpdate):
    item = CrudManager(ConfirmationReceipt).edit_item(session, receipt_id, receipt)
    return item


@per.delete("/receipt/{receipt_id}")
def delete_note(*, session: Session = Depends(get_session), receipt_id: int):
    return CrudManager(Note).delete_item(session, receipt_id)

