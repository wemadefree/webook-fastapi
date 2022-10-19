import datetime
from typing import List, Optional

from app.core.mixins import CamelModelMixin
from pydantic import EmailStr


class PersonBase(CamelModelMixin):
    social_provider_id: Optional[str]
    social_provider_email: Optional[EmailStr]
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
    social_provider_id: Optional[str]
    social_provider_email: Optional[EmailStr]
    personal_email: Optional[EmailStr]
    first_name: Optional[str]
    middle_name: Optional[str]
    last_name: Optional[str]
    birth_date: Optional[datetime.date]


class PersonAddOrUpdate(PersonUpdate):
    id: int
