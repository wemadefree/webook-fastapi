from typing import List
from fastapi import APIRouter, Depends, Query
from sqlmodel import Session

from app.core.session import get_sqlmodel_sesion as get_session
from app.arrangement.model.basemodels import Person, BusinessHour, Note, ConfirmationReceipt, OrganizationType, Organization
from app.arrangement.schema.organizations import BusinessHourRead, BusinessHourUpdate, BusinessHourCreate
from app.arrangement.schema.organizations import OrganizationTypeRead, OrganizationTypeCreate, OrganizationTypeUpdate
from app.arrangement.schema.organizations import OrganizationRead, OrganizationCreate, OrganizationUpdate
from sqlmodel.sql.expression import Select, SelectOfScalar
from app.arrangement.factory import CrudManager

organization_router = org = APIRouter()

SelectOfScalar.inherit_cache = True  # type: ignore
Select.inherit_cache = True  # type: ignore


@org.get("/businesshours", response_model=List[BusinessHourRead])
def read_hours(*, session: Session = Depends(get_session), offset: int = 0, limit: int = Query(default=100, lte=100)):
    hours = CrudManager(BusinessHour).read_items(session, offset, limit)
    return hours


@org.get("/businesshour/{businesshour_id}", response_model=BusinessHourRead)
def read_hour(*, session: Session = Depends(get_session), hour_id: int):
    hour = CrudManager(BusinessHour).read_item(session, hour_id)
    return hour


@org.post("/businesshours/", response_model=BusinessHourRead)
def create_hours(*, session: Session = Depends(get_session), hour: BusinessHourCreate):
    db_hour = CrudManager(BusinessHour).create_item(session, hour)
    return db_hour


@org.patch("/businesshour/{businesshour_id}", response_model=BusinessHourRead)
def update_hour(*, session: Session = Depends(get_session), hour_id: int, hour: BusinessHourUpdate):
    db_hour = CrudManager(BusinessHour).edit_item(session, hour_id, hour)
    return db_hour


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


@org.post("/organizations", response_model=OrganizationRead)
def create_organization(*, session: Session = Depends(get_session), item: OrganizationCreate):
    db_item = CrudManager(Organization).create_item(session, item)
    return db_item


@org.get("/organization/{org_id}", response_model=OrganizationRead)
def read_organization(*, session: Session = Depends(get_session), org_id: int):
    db_item = CrudManager(Organization).read_item(session, org_id)
    return db_item


@org.get("/organizations", response_model=List[OrganizationRead])
def read_organizations(*, session: Session = Depends(get_session), offset: int = 0, limit: int = Query(default=100, lte=100)):
    db_item = CrudManager(Organization).read_item(session, offset, limit)
    return db_item


@org.patch("/organization/{org_id}", response_model=OrganizationRead)
def update_organization(*, session: Session = Depends(get_session), organization_id: int, organization: OrganizationUpdate):
    db_item = CrudManager(Organization).edit_item(session, organization_id, organization)
    return db_item