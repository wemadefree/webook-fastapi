import datetime, enum
from typing import List, Optional
from sqlalchemy import UniqueConstraint
from sqlalchemy.dialects.postgresql import ENUM
from sqlmodel import Column, Field, Relationship, SQLModel, VARCHAR
from pydantic import EmailStr

from app.core.mixins import CamelCaseMixin, TimeStampMixin
from app.arrangement.model.linkmodels import ArrangementNotesLink, ArrangementTimelineEventsLink, ArrangementOwnersLink, ArrangementPeopleParticipantsLink, ArrangementOrganizationParticipantsLink,EventArticlesLink, CalendarPeopleLink, CalendarRoomLink, OrganizationMembersLink, OrganizationNotesLink, PersonNotesLink, PersonBusinessHoursLink, EventRoomLink, EventNotesLink ,EventServiceNotesLink, EventServicePeopleLink, EventLooseServiceRequisitionLink, EventPeopleLink


class StageChoices(str, enum.Enum):
    PLANNING = 'planning'
    REQUISITIONING = 'requisitioning'
    READY_TO_LAUNCH = 'ready_to_launch'
    IN_PRODUCTION = 'in_production'


class Audience(SQLModel, TimeStampMixin, CamelCaseMixin, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(..., max_length=255)
    icon_class: Optional[str] = Field(default='', max_length=255)

    arrangements: List["Arrangement"] = Relationship(back_populates="audience")


class BusinessHour(SQLModel, TimeStampMixin, CamelCaseMixin, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    start_of_business_hours: datetime.time
    end_of_business_hours: datetime.time

    persons: List["Person"] = Relationship(back_populates="businesshours", link_model=PersonBusinessHoursLink)


class Person(SQLModel, TimeStampMixin, CamelCaseMixin, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    personal_email: EmailStr = Field(sa_column=Column("username", VARCHAR, unique=True))
    first_name: str = Field(max_length=255)
    middle_name: str = Field(max_length=255)
    last_name: str = Field(max_length=255)
    birth_date: datetime.date = Field(nullable=True)

    confirmationreceipts: List["ConfirmationReceipt"] = Relationship(back_populates="requested_by")
    calendar_owners: List["Calendar"] = Relationship(back_populates="owner")
    arrangements: List["Arrangement"] = Relationship(back_populates="responsible")

    arrangement_planners: List["Arrangement"] = Relationship(back_populates="planners", link_model=ArrangementOwnersLink)
    arrangement_participants: List["Arrangement"] = Relationship(back_populates="people_participants",link_model=ArrangementPeopleParticipantsLink)

    organization_members: List["Organization"] = Relationship(back_populates="members", link_model=OrganizationMembersLink)

    calendars: List["Calendar"] = Relationship(back_populates="people_resources", link_model=CalendarPeopleLink)
    businesshours: List["BusinessHour"] = Relationship(back_populates="persons", link_model=PersonBusinessHoursLink)
    notes: List["Note"] = Relationship(back_populates="persons", link_model=PersonNotesLink)
    events: List["Event"] = Relationship(back_populates="people", link_model=EventPeopleLink)
    eventservices: List["EventService"] = Relationship(back_populates="associated_people", link_model=EventServicePeopleLink)


class Arrangement(SQLModel, TimeStampMixin, CamelCaseMixin, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=255)
    stages: StageChoices = Field(sa_column=Column(ENUM(StageChoices)), default=StageChoices.PLANNING)
    starts: datetime.date
    ends: datetime.date

    audience_id: Optional[int] = Field(default=None, foreign_key="audience.id")
    responsible_id: Optional[int] = Field(default=None, foreign_key="person.id")

    audience: Optional[Audience] = Relationship(back_populates="arrangements")
    responsible: Optional[Person] = Relationship(back_populates="arrangements")
    looseservicerequisitions: List["LooseServiceRequisition"] = Relationship(back_populates="arrangement")
    eventseries: List["EventSerie"] = Relationship(back_populates="arrangement")
    events: List["Event"] = Relationship(back_populates="arrangement")

    timeline_events: List["TimeLineEvent"] = Relationship(back_populates="arrangements", link_model=ArrangementTimelineEventsLink)
    notes: List["Note"] = Relationship(back_populates="arrangement_notes", link_model=ArrangementNotesLink)
    planners: List["Person"] = Relationship(back_populates="arrangement_planners", link_model=ArrangementOwnersLink)
    people_participants: List["Person"] = Relationship(back_populates="arrangement_participants", link_model=ArrangementPeopleParticipantsLink)
    organization_participants: List["Organization"] = Relationship(back_populates="arrangement_participants", link_model=ArrangementOrganizationParticipantsLink)


class Location(SQLModel, TimeStampMixin, CamelCaseMixin, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    rooms: List["Room"] = Relationship(back_populates="location")


class Room(SQLModel, TimeStampMixin, CamelCaseMixin, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    max_capacity: int = Field(alias="maxCapacity")
    location_id: Optional[int] = Field(foreign_key="location.id", nullable=False)

    location: Optional[Location] = Relationship(back_populates="rooms")

    calendars: List["Calendar"] = Relationship(back_populates="room_resources", link_model=CalendarRoomLink)
    events: List["Event"] = Relationship(back_populates="rooms", link_model=EventRoomLink)


class Article(SQLModel, TimeStampMixin, CamelCaseMixin, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=255)

    events: List["Event"] = Relationship(back_populates="articles", link_model=EventArticlesLink)


class OrganizationType(SQLModel, TimeStampMixin, CamelCaseMixin, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=255)

    organizations: List["Organization"] = Relationship(back_populates="organization_type")


class TimeLineEvent(SQLModel, TimeStampMixin, CamelCaseMixin, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    content: str = Field(max_length=1024)
    stamp: datetime.datetime = Field(nullable=False)

    arrangements: List["Arrangement"] = Relationship(back_populates="timeline_events", link_model=ArrangementTimelineEventsLink)


class ServiceType(SQLModel, TimeStampMixin, CamelCaseMixin, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=255)

    serviceproviders: List["ServiceProvider"] = Relationship(back_populates="service_type")
    looseservicerequisitions: List["LooseServiceRequisition"] = Relationship(back_populates="type_to_order")


class ConfirmationReceipt(SQLModel, TimeStampMixin, CamelCaseMixin, table=True):
    __table_args__ = (UniqueConstraint("guid"),)

    id: Optional[int] = Field(default=None, primary_key=True)
    guid: str = Field(max_length=68, index=True)
    sent_to: str = Field(max_length=255)
    confirmed: bool = Field(default=False)
    sent_when: datetime.datetime = Field(default=None, nullable=True)
    confirmed_when: datetime.datetime = Field(default=None, nullable=True)
    requested_by_id: Optional[int] = Field(default=None, foreign_key="person.id")

    requested_by: Optional[Person] = Relationship(back_populates="confirmationreceipts")
    notes: List["Note"] = Relationship(back_populates="confirmation")
    eventservices: List["EventService"] = Relationship(back_populates="receipt")


class Note(SQLModel, TimeStampMixin, CamelCaseMixin, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    content: str = Field(max_length=1024)

    author_id: Optional[int] = Field(foreign_key="person.id", nullable=False)
    confirmation_id: Optional[int] = Field(default=None, foreign_key="confirmationreceipt.id", nullable=True)

    confirmation: Optional[ConfirmationReceipt] = Relationship(back_populates="notes")
    author: Optional[Person] = Relationship(back_populates="notes")

    persons: List["Person"] = Relationship(back_populates="notes", link_model=PersonNotesLink)
    arrangement_notes: List["Arrangement"] = Relationship(back_populates="notes", link_model=ArrangementNotesLink)
    organization_notes: List["Organization"] = Relationship(back_populates="notes", link_model=OrganizationNotesLink)
    events: List["Event"] = Relationship(back_populates="notes", link_model=EventNotesLink)
    eventservices: List["EventService"] = Relationship(back_populates="notes", link_model=EventServiceNotesLink)


class Organization(SQLModel, TimeStampMixin, CamelCaseMixin, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    organization_number: int = Field(default=None, nullable=True)
    name: str = Field(max_length=255)

    organization_type_id: Optional[int] = Field(foreign_key="organizationtype.id")

    organization_type: Optional[OrganizationType] = Relationship(back_populates="organizations")

    serviceproviders: List["ServiceProvider"] = Relationship(back_populates="organization")

    arrangement_participants: List["Arrangement"] = Relationship(back_populates="organization_participants",
                                                                   link_model=ArrangementOrganizationParticipantsLink)

    members: List["Person"] = Relationship(back_populates="organization_members",
                                                                 link_model=OrganizationMembersLink)

    notes: List["Note"] = Relationship(back_populates="organization_notes",
                                                                 link_model=OrganizationNotesLink)


class Calendar(SQLModel, TimeStampMixin, CamelCaseMixin, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=255)
    is_personal: bool = Field(default=True)

    owner_id: Optional[int] = Field(foreign_key="person.id", nullable=False)

    owner: Optional[Person] = Relationship(back_populates="calendar_owners")

    people_resources: List["Person"] = Relationship(back_populates="calendars", link_model=CalendarPeopleLink)

    room_resources: List["Room"] = Relationship(back_populates="calendars", link_model=CalendarRoomLink)


class ServiceProvider(SQLModel, TimeStampMixin, CamelCaseMixin, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    service_name: str = Field(max_length=255)

    service_type_id: Optional[int] = Field(foreign_key="servicetype.id")
    organization_id: Optional[int] = Field(foreign_key="organization.id")

    service_type: Optional[ServiceType] = Relationship(back_populates="serviceproviders")
    organization: Optional[Organization] = Relationship(back_populates="serviceproviders")
    eventservices: List["EventService"] = Relationship(back_populates="service_provider")


class EventSerie(SQLModel, TimeStampMixin, CamelCaseMixin, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    arrangement_id: Optional[int] = Field(foreign_key="arrangement.id")

    arrangement: Optional[Arrangement] = Relationship(back_populates="eventseries")

    events: List["Event"] = Relationship(back_populates="serie")


class Event(SQLModel, TimeStampMixin, CamelCaseMixin, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(max_length=255)
    start: datetime.datetime = Field(nullable=False)
    end: datetime.datetime = Field(nullable=False)
    all_day: bool = Field(default=False)
    sequence_guid: str = Field(max_length=40, nullable=True)
    color: str = Field(max_length=40, nullable=True)

    serie_id: Optional[int] = Field(foreign_key="eventserie.id", nullable=True, default=None)
    arrangement_id: Optional[int] = Field(foreign_key="arrangement.id")

    serie: Optional[EventSerie] = Relationship(back_populates="events")
    arrangement: Optional[Arrangement] = Relationship(back_populates="events")
    eventservices: List["EventService"] = Relationship(back_populates="event")

    people: List["Person"] = Relationship(back_populates="events", link_model=EventPeopleLink)
    rooms: List["Room"] = Relationship(back_populates="events", link_model=EventRoomLink)
    loose_requisitions: List["LooseServiceRequisition"] = Relationship(back_populates="events", link_model=EventLooseServiceRequisitionLink)
    articles: List["Article"] = Relationship(back_populates="events", link_model=EventArticlesLink)
    notes: List["Note"] = Relationship(back_populates="events", link_model=EventNotesLink)


class EventService(SQLModel, TimeStampMixin, CamelCaseMixin, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    receipt_id: Optional[int] = Field(foreign_key="confirmationreceipt.id")
    event_id: Optional[int] = Field(foreign_key="event.id")
    service_provider_id: Optional[int] = Field(foreign_key="serviceprovider.id")

    receipt: Optional[ConfirmationReceipt] = Relationship(back_populates="eventservices")
    event: Optional[Event] = Relationship(back_populates="eventservices")
    service_provider: Optional[ServiceProvider] = Relationship(back_populates="eventservices")

    notes: List["Note"] = Relationship(back_populates="eventservices", link_model=EventServiceNotesLink)
    associated_people: List["Person"] = Relationship(back_populates="eventservices", link_model=EventServicePeopleLink)


class LooseServiceRequisition(SQLModel, TimeStampMixin, CamelCaseMixin, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    comment: str = Field(default='')

    arrangement_id: Optional[int] = Field(foreign_key="arrangement.id")
    type_to_order_id: Optional[int] = Field(foreign_key="servicetype.id")

    arrangement: Optional[Arrangement] = Relationship(back_populates="looseservicerequisitions")
    type_to_order: Optional[ServiceType] = Relationship(back_populates="looseservicerequisitions")

    events: List["Event"] = Relationship(back_populates="loose_requisitions",
                                                                       link_model=EventLooseServiceRequisitionLink)
