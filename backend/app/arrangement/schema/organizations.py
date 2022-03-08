import datetime
from typing import Optional, List
from sqlmodel import SQLModel

from app.core.mixins import CamelCaseMixin
from app.arrangement.schema.persons import PersonRead, NoteRead


class OrganizationTypeBase(SQLModel, CamelCaseMixin):
    name: str


class OrganizationTypeCreate(OrganizationTypeBase):
    pass


class OrganizationTypeRead(OrganizationTypeBase):
    id: int


class OrganizationTypeUpdate(SQLModel):
    name: Optional[str] = None


class OrganizationBase(SQLModel, CamelCaseMixin):
    name: str
    organization_number: int
    organization_type_id: Optional[int]


class OrganizationCreate(OrganizationBase):
    pass


class OrganizationRead(OrganizationBase):
    id: int
    organization_type: Optional[OrganizationTypeRead] = None


class OrganizationReadExtra(OrganizationRead):
    members: List[PersonRead]
    notes: List[NoteRead]


class OrganizationUpdate(SQLModel, CamelCaseMixin):
    name:  Optional[str]
    organization_number:  Optional[int]
    organization_type_id: Optional[int]


class OrganizationAddOrUpdate(SQLModel, CamelCaseMixin):
    id: int
    name:  Optional[str]
    organization_number:  Optional[int]
    organization_type_id: Optional[int]