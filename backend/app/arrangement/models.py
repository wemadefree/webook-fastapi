import datetime
from typing import List, Optional
from sqlalchemy import UniqueConstraint
from sqlmodel import Column, Field, Relationship, SQLModel, VARCHAR
from pydantic import EmailStr

from app.core.mixins import CamelCaseMixin, TimeStampMixin


class ArrangementOwnersLink(SQLModel, table=True):
    __tablename__ = "arrangement_owners"

    id: Optional[int] = Field(default=None, primary_key=True)
    arrangement_id: Optional[int] = Field(foreign_key="arrangement.id", nullable=False)
    person_id: Optional[int] = Field(foreign_key="person.id", nullable=False)


class ArrangementPeopleParticipantsLink(SQLModel, table=True):
    __tablename__ = "arrangement_people_participants"

    id: Optional[int] = Field(default=None, primary_key=True)
    arrangement_id: Optional[int] = Field(foreign_key="arrangement.id", nullable=False)
    person_id: Optional[int] = Field(foreign_key="person.id", nullable=False)


class PersonNotesLink(SQLModel, table=True):
    __tablename__ = "person_notes"

    id: Optional[int] = Field(default=None, primary_key=True)
    note_id: Optional[int] = Field(foreign_key="note.id", nullable=False)
    person_id: Optional[int] = Field(foreign_key="person.id", nullable=False)


class ArrangementOrganizationParticipantsLink(SQLModel, table=True):
    __tablename__ = "arrangement_organization_participants"

    id: Optional[int] = Field(default=None, primary_key=True)
    arrangement_id: Optional[int] = Field(foreign_key="arrangement.id", nullable=False)
    organization_id: Optional[int] = Field(foreign_key="organization.id", nullable=False)


class ArrangementTimelineEventsLink(SQLModel, table=True):
    __tablename__ = "arrangement_timeline_events"

    id: Optional[int] = Field(default=None, primary_key=True)
    arrangement_id: Optional[int] = Field(foreign_key="arrangement.id", nullable=False)
    timelineevent_id: Optional[int] = Field(foreign_key="timelineevent.id", nullable=False)


class CalendarPeopleLink(SQLModel, table=True):
    __tablename__ = "calendar_people_resources"

    id: Optional[int] = Field(default=None, primary_key=True)
    calendar_id: Optional[int] = Field(foreign_key="calendar.id", nullable=False)
    person_id: Optional[int] = Field(foreign_key="person.id", nullable=False)


class CalendarRoomLink(SQLModel, table=True):
    __tablename__ = "calendar_room_resources"

    id: Optional[int] = Field(default=None, primary_key=True)
    calendar_id: Optional[int] = Field(foreign_key="calendar.id", nullable=False)
    room_id: Optional[int] = Field(foreign_key="room.id", nullable=False)


class EventArticlesLink(SQLModel, table=True):
    __tablename__ = "event_articles"

    id: Optional[int] = Field(default=None, primary_key=True)
    event_id: Optional[int] = Field(foreign_key="event.id", nullable=False)
    article_id: Optional[int] = Field(foreign_key="article.id", nullable=False)


class EventNotesLink(SQLModel, table=True):
    __tablename__ = "event_notes"

    id: Optional[int] = Field(default=None, primary_key=True)
    event_id: Optional[int] = Field(foreign_key="event.id", nullable=False)
    note_id: Optional[int] = Field(foreign_key="note.id", nullable=False)


class EventPeopleLink(SQLModel, table=True):
    __tablename__ = "event_people"

    id: Optional[int] = Field(default=None, primary_key=True)
    event_id: Optional[int] = Field(foreign_key="event.id", nullable=False)
    person_id: Optional[int] = Field(foreign_key="person.id", nullable=False)


class EventRoomLink(SQLModel, table=True):
    __tablename__ = "event_rooms"

    id: Optional[int] = Field(default=None, primary_key=True)
    event_id: Optional[int] = Field(foreign_key="event.id", nullable=False)
    room_id: Optional[int] = Field(foreign_key="room.id", nullable=False)


class EventServicePeopleLink(SQLModel, table=True):
    __tablename__ = "eventservice_associated_people"

    id: Optional[int] = Field(default=None, primary_key=True)
    eventservice_id: Optional[int] = Field(foreign_key="eventservice.id", nullable=False)
    person_id: Optional[int] = Field(foreign_key="person.id", nullable=False)


class EventServiceNotesLink(SQLModel, table=True):
    __tablename__ = "eventservice_notes"

    id: Optional[int] = Field(default=None, primary_key=True)
    eventservice_id: Optional[int] = Field(foreign_key="eventservice.id", nullable=False)
    note_id: Optional[int] = Field(foreign_key="note.id", nullable=False)


class OrganizationMembersLink(SQLModel, table=True):
    __tablename__ = "organization_members"

    id: Optional[int] = Field(default=None, primary_key=True)
    organization_id: Optional[int] = Field(foreign_key="organization.id", nullable=False)
    person_id: Optional[int] = Field(foreign_key="person.id", nullable=False)


class OrganizationNotesLink(SQLModel, table=True):
    __tablename__ = "organization_notes"

    id: Optional[int] = Field(default=None, primary_key=True)
    organization_id: Optional[int] = Field(foreign_key="organization.id", nullable=False)
    note_id: Optional[int] = Field(foreign_key="note.id", nullable=False)


class EventLooseServiceRequisitionLink(SQLModel, table=True):
    __tablename__ = "event_looseservicerequisition"

    id: Optional[int] = Field(default=None, primary_key=True)
    event_id: Optional[int] = Field(foreign_key="event.id", nullable=False)
    looseservicerequisition_id: Optional[int] = Field(foreign_key="looseservicerequisition.id", nullable=False)


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


class Audience(SQLModel, TimeStampMixin, CamelCaseMixin, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(..., max_length=255)
    icon_class: Optional[str] = Field(default='', max_length=255)


class Article(SQLModel, TimeStampMixin, CamelCaseMixin, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=255)


class OrganizationType(SQLModel, TimeStampMixin, CamelCaseMixin, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=255)


class TimeLineEvent(SQLModel, TimeStampMixin, CamelCaseMixin, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    content: str = Field(max_length=1024)
    stamp: datetime.datetime = Field(nullable=False)


class ServiceType(SQLModel, TimeStampMixin, CamelCaseMixin, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=255)


class BusinessHour(SQLModel, TimeStampMixin, CamelCaseMixin, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    start_of_business_hours: datetime.time
    end_of_business_hours: datetime.time


class Person(SQLModel, TimeStampMixin, CamelCaseMixin, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    personal_email: EmailStr = Field(sa_column=Column("username", VARCHAR, unique=True))
    first_name: str = Field(max_length=255)
    middle_name: str = Field(max_length=255)
    last_name: str = Field(max_length=255)
    birth_date: datetime.date = Field(nullable=True)

    business_hour_id: Optional[int] = Field(default=None, foreign_key="businesshour.id", nullable=True)

    business_hour: Optional[BusinessHour] = Relationship(back_populates="businesshours")

    notes: List["Note"] = Relationship(back_populates="persons", link_model=PersonNotesLink)


class Arrangement(SQLModel, TimeStampMixin, CamelCaseMixin, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=255)
    starts: datetime.date
    ends: datetime.date

    audience_id: Optional[int] = Field(default=None, foreign_key="audience.id")
    responsible_id: Optional[int] = Field(default=None, foreign_key="person.id")

    audience: Optional[Audience] = Relationship(back_populates="arrangements")
    responsible: Optional[Person] = Relationship(back_populates="arrangements")

    timeline_events: List["TimeLineEvent"] = Relationship(back_populates="arrangements",
                                                          link_model=ArrangementTimelineEventsLink)

    notes: List["Note"] = Relationship(back_populates="arrangements", link_model=PersonNotesLink)

    owners: List["Person"] = Relationship(back_populates="arrangements", link_model=ArrangementOwnersLink)

    people_participants: List["Person"] = Relationship(back_populates="arrangements",
                                                       link_model=ArrangementPeopleParticipantsLink)

    organization_participants: List["Organization"] = Relationship(back_populates="arrangements",
                                                                   link_model=ArrangementOrganizationParticipantsLink)


class Calendar(SQLModel, TimeStampMixin, CamelCaseMixin, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=255)
    is_personal: bool = Field(default=True)

    owner_id: Optional[int] = Field(foreign_key="person.id", nullable=False)

    owner: Optional[Person] = Relationship(back_populates="calendars")

    people_resources: List["Person"] = Relationship(back_populates="calendars", link_model=CalendarPeopleLink)

    room_resources: List["Room"] = Relationship(back_populates="calendars", link_model=CalendarRoomLink)


class ConfirmationReceipt(SQLModel, TimeStampMixin, CamelCaseMixin, table=True):
    __table_args__ = (UniqueConstraint("guid"),)

    id: Optional[int] = Field(default=None, primary_key=True)
    guid: str = Field(max_length=68, index=True)
    sent_to: str = Field(max_length=255)
    confirmed: bool = Field(default=False)
    sent_when: datetime.datetime = Field(default=None)
    confirmed_when: datetime.datetime = Field(default=None)

    requested_by_id: Optional[int] = Field(default=None, foreign_key="person.id")

    requested_by: Optional[Person] = Relationship(back_populates="confirmationreceipts")


class Note(SQLModel, TimeStampMixin, CamelCaseMixin, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    content: str = Field(max_length=1024)

    author_id: Optional[int] = Field(foreign_key="person.id", nullable=False)
    confirmation_id: Optional[int] = Field(default=None, foreign_key="confirmationreceipt.id")

    confirmation: Optional[ConfirmationReceipt] = Relationship(back_populates="notes")
    author: Optional[Person] = Relationship(back_populates="notes")


class Organization(SQLModel, TimeStampMixin, CamelCaseMixin, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    organization_number: int = Field(nullable=True)
    name: str = Field(max_length=255)

    organization_type_id: Optional[int] = Field(foreign_key="organizationtype.id")

    organization_type: Optional[OrganizationType] = Relationship(back_populates="organizations")

    notes: List["Note"] = Relationship(back_populates="organizations", link_model=OrganizationNotesLink)

    members: List["Person"] = Relationship(back_populates="organizations", link_model=OrganizationMembersLink)


class ServiceProvider(SQLModel, TimeStampMixin, CamelCaseMixin, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    service_name: str = Field(max_length=255)

    service_type_id: Optional[int] = Field(foreign_key="servicetype.id")
    organization_id: Optional[int] = Field(foreign_key="organization.id")

    service_type: Optional[ServiceType] = Relationship(back_populates="serviceproviders")
    organization: Optional[Organization] = Relationship(back_populates="serviceproviders")


class EventSerie(SQLModel, TimeStampMixin, CamelCaseMixin, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    arrangement_id: Optional[int] = Field(foreign_key="arrangement.id")

    arrangement: Optional[Arrangement] = Relationship(back_populates="eventseries")


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
    comment: str

    arrangement_id: Optional[int] = Field(foreign_key="arrangement.id")
    type_to_order_id: Optional[int] = Field(foreign_key="servicetype.id")

    arrangement: Optional[Arrangement] = Relationship(back_populates="looseservicerequisitions")
    type_to_order: Optional[ServiceType] = Relationship(back_populates="looseservicerequisitions")
