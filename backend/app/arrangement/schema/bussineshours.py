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


class BusinessHourAddOrUpdate(BusinessHourUpdate):
    id: int