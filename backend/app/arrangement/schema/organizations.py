import datetime
from typing import Optional, List

from app.core.mixins import CamelModelMixin
from app.arrangement.schema.persons import PersonRead


class OrganizationTypeBase(CamelModelMixin):
    name: str

    class Config:
        orm_mode = True


class OrganizationTypeCreate(OrganizationTypeBase):
    pass


class OrganizationTypeRead(OrganizationTypeBase):
    id: int


class OrganizationTypeUpdate(CamelModelMixin):
    name: Optional[str] = None


class OrganizationBase(CamelModelMixin):
    name: str
    organization_number: Optional[int]
    organization_type_id: Optional[int]

    class Config:
        orm_mode = True


class OrganizationCreate(OrganizationBase):
    pass


class OrganizationRead(OrganizationBase):
    id: int
    organization_type: Optional[OrganizationTypeRead] = None


class OrganizationReadExtra(OrganizationRead):
    members: List[PersonRead]
    #notes: List[NoteRead]


class OrganizationUpdate(CamelModelMixin):
    name:  Optional[str]
    organization_number:  Optional[int]
    organization_type_id: Optional[int]


class OrganizationAddOrUpdate(CamelModelMixin):
    id: int
    name:  Optional[str]
    organization_number:  Optional[int]
    organization_type_id: Optional[int]