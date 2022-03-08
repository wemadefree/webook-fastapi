import datetime
from typing import List, Optional
from sqlmodel import SQLModel

from app.arrangement.schema.persons import PersonRead
from app.arrangement.schema.rooms import RoomRead
from app.core.mixins import CamelCaseMixin


class CalendarBase(SQLModel, CamelCaseMixin):
    name: str
    is_personal: bool
    owner_id: Optional[int]


class CalendarRead(CalendarBase):
    id: int


class CalendarCreate(CalendarBase):
    pass


class CalendarUpdate(SQLModel, CamelCaseMixin):
    name: Optional[str]
    is_personal: Optional[bool]
    owner_id: Optional[int]


class CalendarReadExtra(SQLModel, CamelCaseMixin):
    name: Optional[str]
    is_personal: Optional[bool]
    owner_id: Optional[int]
    owner: Optional[PersonRead]
    people_resources: List[PersonRead]
    room_resources: List[RoomRead]