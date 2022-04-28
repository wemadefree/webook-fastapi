import datetime
from typing import List, Optional
from sqlmodel import SQLModel
from pydantic import EmailStr

from app.core.mixins import CamelCaseMixin


class ConfirmationRecieptBase(SQLModel, CamelCaseMixin):
    guid: str
    sent_to: str
    confirmed: bool
    sent_when: Optional[datetime.datetime]
    confirmed_when: Optional[datetime.datetime]
    requested_by_id: Optional[int]


class ConfirmationRecieptRead(ConfirmationRecieptBase):
    id: int


class ConfirmationRecieptCreate(ConfirmationRecieptBase):
    pass


class ConfirmationRecieptUpdate(SQLModel, CamelCaseMixin):
    guid: Optional[str]
    sent_to: Optional[str]
    confirmed: Optional[bool]
    sent_when: Optional[datetime.datetime]
    confirmed_when: Optional[datetime.datetime]
    requested_by_id: Optional[int]


class NoteBase(SQLModel, CamelCaseMixin):
    content: str
    author_id: Optional[int]
    confirmation_id: Optional[int]


class NoteRead(NoteBase):
    id: int


class NoteCreate(NoteBase):
    pass


class NoteUpdate(SQLModel, CamelCaseMixin):
    content: Optional[str]
    author_id: Optional[int]
    confirmation_id: Optional[int]


class NoteAddOrUpdate(NoteUpdate):
    id: int


class NoteCreateOrUpdate(SQLModel, CamelCaseMixin):
    id: int
    content: Optional[str]
    author_id: Optional[int]
    confirmation_id: Optional[int]


class PersonBase(SQLModel, CamelCaseMixin):
    personal_email: Optional[str]
    first_name: str
    middle_name: Optional[str]
    last_name: str
    birth_date: Optional[datetime.date]


class PersonRead(PersonBase):
    id: int


class PersonCreate(PersonBase):
    pass


class PersonReadExtra(PersonRead):
    #notes: List[NoteRead]
    #businesshours: List[BusinessHourRead]
    pass

class PersonReadWithHours(PersonRead):
    #notes: List[NoteRead] = []
    #businesshours: List[BusinessHourRead] = []
    pass

class PersonCreateWithNotes(PersonBase):
    #notes: List[NoteBase] = []
    #businesshours: List[BusinessHourBase] = []
    pass

class PersonUpdate(SQLModel, CamelCaseMixin):
    personal_email: Optional[EmailStr]
    first_name: Optional[str]
    middle_name: Optional[str]
    last_name: Optional[str]
    birth_date: Optional[datetime.date]


class PersonAddOrUpdate(PersonUpdate):
    id: int


class PersonUpdateWithNotes(PersonUpdate):
    notes: Optional[List[NoteUpdate]]
    #businesshours: Optional[List[BusinessHourUpdate]]


class ConfirmationRecieptWithNoteAndAuthors(ConfirmationRecieptRead):
    notes: List[NoteRead] = []
    requested_by: Optional[PersonRead] = None


class NoteReadWithAuthors(NoteRead):
    person_notes: List[PersonRead] = []
    confirmation: Optional[ConfirmationRecieptRead] = None