from typing import List
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlmodel.sql.expression import Select, SelectOfScalar

from app.core.session import get_session
from app.arrangement.model.basemodels import Person, Audience, OrganizationType, Organization
from app.arrangement.schema.persons import PersonRead, PersonReadExtra, PersonCreate, PersonUpdate, PersonReadWithHours
from app.arrangement.factory import CrudManager


person_router = per = APIRouter()
note_router = nt = APIRouter()
receipt_router = rec = APIRouter()

#SelectOfScalar.inherit_cache = True  # type: ignore
#Select.inherit_cache = True  # type: ignore


@per.post("/persons", response_model=PersonRead)
def create_person(*, session: Session = Depends(get_session), person: PersonCreate):
    db_person = CrudManager(Person).create_item(session, person)
    return db_person


@per.patch("/person/{person_id}", response_model=PersonRead)
def update_person(*, session: Session = Depends(get_session), person_id: int, person: PersonUpdate):
    db_person = CrudManager(Person).edit_item(session, person_id, person)
    return db_person

"""
@per.post("/person/{person_id}/note/{note_id}", response_model=PersonReadExtra)
def add_note_for_person(*, session: Session = Depends(get_session), person_id: int, note_id: int):
    db_person = CrudManager(Person).read_item(session, person_id)
    if db_person:
        db_note = CrudManager(Note).read_item(session, note_id)
        if db_note:
            db_person.notes.append(db_note)
        db_person = CrudManager(Person).edit_item(session, person_id, db_person)
    return db_person


@per.delete("/person/{person_id}/note/{note_id}", response_model=PersonReadExtra)
def remove_note_from_person(*, session: Session = Depends(get_session), person_id: int, note_id: int):
    db_cal = CrudManager(Person).read_item(session, person_id)
    if db_cal:
        for per in db_cal.notes:
            if per.id == note_id:
                db_cal.notes.remove(per)
                break
        db_cal = CrudManager(Person).edit_item(session, person_id, db_cal)
    return db_cal

"""

@per.get("/person/{person_id}", response_model=PersonReadExtra)
def read_person(*, session: Session = Depends(get_session), person_id: int):
    item = CrudManager(Person).read_item(session, person_id)
    return item


@per.get("/persons", response_model=List[PersonRead])
def list_persons(*, session: Session = Depends(get_session), offset: int = 0, limit: int = Query(default=100, lte=100)):
    item = CrudManager(Person).read_items(session, offset, limit)
    return item


@per.delete("/person/{person_id}")
def delete_person(*, session: Session = Depends(get_session), person_id: int):
    return CrudManager(Person).delete_item(session, person_id)


