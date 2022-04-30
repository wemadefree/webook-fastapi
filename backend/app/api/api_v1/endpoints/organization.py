from typing import List
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.core.session import get_session
from app.arrangement.model.basemodels import Person, OrganizationType, Organization
from app.arrangement.schema.organizations import OrganizationTypeRead, OrganizationTypeCreate, OrganizationTypeUpdate
from app.arrangement.schema.organizations import OrganizationRead, OrganizationReadExtra, OrganizationCreate, OrganizationUpdate, OrganizationAddOrUpdate
from app.arrangement.factory import CrudManager

organization_router = org = APIRouter()
hour_router = hour = APIRouter()

#SelectOfScalar.inherit_cache = True  # type: ignore
#Select.inherit_cache = True  # type: ignore


@org.post("/orgtypes", response_model=OrganizationTypeRead)
def create_organization_type(*, session: Session = Depends(get_session), item: OrganizationTypeCreate):
    db_item = CrudManager(OrganizationType).create_item(session, item)
    return db_item


@org.get("/orgtypes/{org_type_id}", response_model=OrganizationTypeRead)
def read_organization_type(*, session: Session = Depends(get_session), org_type_id: int):
    db_item = CrudManager(OrganizationType).read_item(session, org_type_id)
    return db_item


@org.get("/orgtypes", response_model=List[OrganizationTypeRead])
def read_organization_types(*, session: Session = Depends(get_session), offset: int = 0, limit: int = Query(default=100, lte=100)):
    db_item = CrudManager(OrganizationType).read_items(session, offset, limit)
    return db_item


@org.patch("/orgtypes/{org_type_id}", response_model=OrganizationTypeRead)
def update_organization_type(*, session: Session = Depends(get_session), org_type_id: int, org_type: OrganizationTypeUpdate):
    db_item = CrudManager(OrganizationType).edit_item(session, org_type_id, org_type)
    return db_item


@org.delete("/orgtypes/{org_type_id}")
def delete_organization_type(*, session: Session = Depends(get_session), org_type_id: int):
    return CrudManager(OrganizationType).delete_item(session, org_type_id)


@org.post("/organizations", response_model=OrganizationRead)
def create_organization(*, session: Session = Depends(get_session), item: OrganizationCreate):
    db_item = CrudManager(Organization).create_item(session, item)
    return db_item


@org.get("/organization/{org_id}", response_model=OrganizationReadExtra)
def read_organization(*, session: Session = Depends(get_session), org_id: int):
    db_item = CrudManager(Organization).read_item(session, org_id)
    return db_item


@org.get("/organizations", response_model=List[OrganizationRead])
def read_organizations(*, session: Session = Depends(get_session), offset: int = 0, limit: int = Query(default=100, lte=100)):
    db_item = CrudManager(Organization).read_items(session, offset, limit)
    return db_item


@org.patch("/organization/{org_id}", response_model=OrganizationReadExtra)
def update_organization(*, session: Session = Depends(get_session), organization_id: int, organization: OrganizationUpdate):
    db_item = CrudManager(Organization).edit_item(session, organization_id, organization)
    return db_item


@org.delete("/organization/{org_id}")
def delete_organization(*, session: Session = Depends(get_session), org_id: int):
    return CrudManager(Organization).delete_item(session, org_id)


@org.post("/organization/{org_id}/member/{person_id}", response_model=OrganizationReadExtra)
def add_member_to_organization(*, session: Session = Depends(get_session), org_id: int, person_id: int):
    db_cal = CrudManager(Organization).read_item(session, org_id)
    if db_cal:
        db_person = CrudManager(Person).read_item(session, person_id)
        if db_person:
            db_cal.members.append(db_person)
        db_cal = CrudManager(Organization).edit_item(session, org_id, db_cal)
    return db_cal


@org.delete("/organization/{org_id}/member/{person_id}", response_model=OrganizationReadExtra)
def remove_member_from_organization(*, session: Session = Depends(get_session), org_id: int, person_id: int):
    db_organization = CrudManager(Organization).read_item(session, org_id)
    if db_organization:
        for per in db_organization.members:
            if per.id == person_id:
                db_organization.members.remove(per)
                break
        db_organization = CrudManager(Organization).edit_item(session, person_id, db_organization)
    return db_organization


@org.post("/organization/{org_id}/note/{note_id}", response_model=OrganizationReadExtra)
def add_note_to_organization(*, session: Session = Depends(get_session), organization_id: int, note_id: int):
    db_organization = CrudManager(Organization).read_item(session, organization_id)
    if db_organization:
        db_note = CrudManager(Note).read_item(session, note_id)
        if db_note:
            db_organization.notes.append(db_note)
        db_organization = CrudManager(Organization).edit_item(session, organization_id, db_organization)
    return db_organization


@org.delete("/organization/{org_id}/note/{note_id}", response_model=OrganizationReadExtra)
def delete_note_from_organization(*, session: Session = Depends(get_session), organization_id: int, note_id: int):
    db_organization = CrudManager(Organization).read_item(session, organization_id)
    if db_organization:
        for per in db_organization.notes:
            if per.id == note_id:
                db_organization.notes.remove(per)
                break
        db_organization = CrudManager(Organization).edit_item(session, note_id, db_organization)
    return db_organization
