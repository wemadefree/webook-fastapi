import datetime
from typing import List, Optional
from pydantic import EmailStr

from app.core.mixins import CamelModelMixin


class PersonBase(CamelModelMixin):
    personal_email: Optional[str]
    first_name: str
    middle_name: Optional[str]
    last_name: str
    birth_date: Optional[datetime.date]
    slug: Optional[str]

    class Config:
        orm_mode = True


class PersonRead(PersonBase):
    id: int


class PersonCreate(PersonBase):
    pass


class PersonReadExtra(PersonRead):
    pass


class PersonReadWithHours(PersonRead):
    pass


class PersonCreateWithNotes(PersonBase):
    pass


class PersonUpdate(CamelModelMixin):
    personal_email: Optional[EmailStr]
    first_name: Optional[str]
    middle_name: Optional[str]
    last_name: Optional[str]
    birth_date: Optional[datetime.date]


class PersonAddOrUpdate(PersonUpdate):
    id: int
