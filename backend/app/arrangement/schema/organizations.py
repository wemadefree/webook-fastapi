import datetime
from typing import Optional
from sqlmodel import SQLModel

from app.core.mixins import CamelCaseMixin


class BusinessHourBase(SQLModel, CamelCaseMixin):
    start_of_business_hours: datetime.time
    end_of_business_hours: datetime.time


class BusinessHourRead(BusinessHourBase):
    id: int


class BusinessHourCreate(BusinessHourBase):
    pass


class BusinessHourUpdate(SQLModel, CamelCaseMixin):
    start_of_business_hours: Optional[datetime.time]
    end_of_business_hours: Optional[datetime.time]


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


class OrganizationUpdate(SQLModel, CamelCaseMixin):
    name:  Optional[str]
    organization_number:  Optional[int]
    organization_type_id: Optional[int]