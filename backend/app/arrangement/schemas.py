import datetime
from typing import List, Optional
from sqlmodel import Field, SQLModel
from pydantic import EmailStr

from app.arrangement.model.basemodels import StageChoices
from app.core.mixins import CamelCaseMixin


class AudienceBase(SQLModel, CamelCaseMixin):
    name: str
    icon_class: str


class AudienceRead(AudienceBase):
    id: int


class AudienceCreate(AudienceBase):
    pass


class AudienceUpdate(SQLModel, CamelCaseMixin):
    name: Optional[str]
    icon_class: Optional[str]


class LocationBase(SQLModel, CamelCaseMixin):
    name: str


class LocationCreate(LocationBase):
    pass


class LocationRead(LocationBase):
    id: int


class LocationUpdate(SQLModel):
    name: Optional[str] = None


class RoomBase(SQLModel, CamelCaseMixin):
    name: str
    max_capacity: int
    location_id: Optional[int]


class RoomCreate(RoomBase):
    pass


class RoomRead(RoomBase):
    id: int


class RoomUpdate(SQLModel, CamelCaseMixin):
    name: Optional[str] = None
    max_capacity: Optional[int]
    location_id: Optional[int]


class RoomReadWithLocation(RoomRead):
    location: Optional[LocationRead] = None


class LocationReadWithRoom(LocationRead):
    rooms: List[RoomRead] = []


class PersonBase(SQLModel, CamelCaseMixin):
    personal_email: EmailStr
    first_name: str
    middle_name: str
    last_name: str
    birth_date: datetime.date


class PersonRead(PersonBase):
    id: int


class PersonCreate(PersonBase):
    pass


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


class NoteBase(SQLModel, CamelCaseMixin):
    content: str = Field(max_length=1024)
    author_id: Optional[int]
    confirmation_id: Optional[int]


class NoteRead(NoteBase):
    id: int


class NoteCreate(NoteBase):
    pass


class NoteUpdate(SQLModel, CamelCaseMixin):
    id: int
    content: Optional[str]
    author_id: Optional[int]
    confirmation_id: Optional[int]


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


class ConfirmationRecieptWithNoteAndAuthors(ConfirmationRecieptRead):
    notes: List[NoteRead] = []
    requested_by: Optional[PersonRead] = None


class NoteReadWithAuthors(NoteRead):
    person_notes: List[PersonRead] = []
    confirmation: Optional[ConfirmationRecieptRead] = None


class PersonReadWithHours(PersonRead):
    notes: List[NoteRead] = []
    businesshours: List[BusinessHourRead] = []


class PersonCreateWithNotes(PersonBase):
    notes: List[NoteBase] = []
    businesshours: List[BusinessHourBase] = []


class PersonUpdate(SQLModel, CamelCaseMixin):
    id: int
    personal_email: Optional[EmailStr]
    first_name: Optional[str]
    middle_name: Optional[str]
    last_name: Optional[str]
    birth_date: Optional[datetime.date]


class PersonUpdateWithNotes(PersonUpdate):
    notes: Optional[List[NoteUpdate]]
    businesshours: Optional[List[BusinessHourUpdate]]


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


class TimeLineEventBase(SQLModel, CamelCaseMixin):
    content: str
    stamp: datetime.datetime


class TimeLineEventCreate(TimeLineEventBase):
    pass


class TimeLineEventRead(TimeLineEventBase):
    id: int


class TimeLineEventUpdate(SQLModel, CamelCaseMixin):
    content: Optional[str]
    stamp: Optional[datetime.datetime]


class ArrangementBase(SQLModel, CamelCaseMixin):
    name: str
    stages: StageChoices
    starts: datetime.date
    ends: datetime.date
    audience_id: Optional[int]
    responsible_id: Optional[int]


class ArrangementCreate(ArrangementBase):
    pass


class ArrangementRead(ArrangementBase):
    id: int
    audience: Optional[AudienceRead] = None
    responsible: Optional[PersonRead] = None

    timeline_events: List[TimeLineEventRead] = []
    planners: List[PersonRead] = []
    people_participants: List[PersonRead] = []
    organization_participants: List[OrganizationRead] = []
    notes: List[NoteRead] = []


class ArrangementUpdate(SQLModel, CamelCaseMixin):
    name: Optional[str]
    stages: Optional[StageChoices]
    starts: Optional[datetime.date]
    ends: Optional[datetime.date]
    audience_id: Optional[int]
    responsible_id: Optional[int]
    notes: Optional[List[NoteUpdate]]


