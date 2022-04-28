import datetime, enum
from pydantic import EmailStr
from sqlalchemy import UniqueConstraint
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.orm import column_property, declared_attr, relationship, backref
from sqlmodel import Column, Field, Relationship, SQLModel, VARCHAR
from slugify import slugify
from typing import List, Optional


from app.core.mixins import CamelCaseMixin, TimeStampMixin
from app.arrangement.model.linkmodels import (
    ArrangementNotesLink, ArrangementDisplayLayout, ArrangementTimelineEventsLink, ArrangementOwnersLink,
    ArrangementPeopleParticipantsLink, ArrangementOrganizationParticipantsLink,EventArticlesLink,
    EventDisplayLayout, CalendarPeopleLink, CalendarRoomLink, OrganizationMembersLink, OrganizationNotesLink,
    PersonNotesLink, EventRoomLink, EventNotesLink ,EventServiceNotesLink, EventServicePeopleLink,
    EventLooseServiceRequisitionLink, EventPeopleLink, RoomPresetLink
    )


class StageChoices():
    PLANNING = 'planning'
    REQUISITIONING = 'requisitioning'
    READY_TO_LAUNCH = 'ready_to_launch'
    IN_PRODUCTION = 'in_production'


class Audience(SQLModel, TimeStampMixin, CamelCaseMixin, table=True):
    __tablename__ = "arrangement_audience"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(..., max_length=255)
    name_en: str = Field(max_length=255, nullable=True)
    icon_class: Optional[str] = Field(default='', max_length=255)

    arrangements: List["Arrangement"] = Relationship(back_populates="audience")

"""
class BusinessHour(SQLModel, TimeStampMixin, CamelCaseMixin, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    start_of_business_hours: datetime.time
    end_of_business_hours: datetime.time

    persons: List["Person"] = Relationship(back_populates="businesshours", link_model=PersonBusinessHoursLink)
"""


class Person(SQLModel, TimeStampMixin, CamelCaseMixin, table=True):
    __tablename__ = "arrangement_person"

    id: Optional[int] = Field(default=None, primary_key=True)
    personal_email: Optional[EmailStr] = Field(default=None)
    first_name: str = Field(max_length=255)
    middle_name: str = Field(max_length=255)
    last_name: str = Field(max_length=255)
    birth_date: datetime.date = Field(nullable=True)

    confirmationreceipts: List["ConfirmationReceipt"] = Relationship(back_populates="requested_by")
    calendar_owners: List["Calendar"] = Relationship(back_populates="owner")
    arrangements: List["Arrangement"] = Relationship(back_populates="responsible")

    author_notes: List["Note"] = Relationship(back_populates="author")

    arrangement_planners: List["Arrangement"] = Relationship(
        back_populates="planners",
        link_model=ArrangementOwnersLink,
    )
    arrangement_participants: List["Arrangement"] = Relationship(
        back_populates="people_participants",
        link_model=ArrangementPeopleParticipantsLink,
    )
    organization_members: List["Organization"] = Relationship(
        back_populates="members",
        link_model=OrganizationMembersLink,
    )
    calendars: List["Calendar"] = Relationship(
        back_populates="people_resources",
        link_model=CalendarPeopleLink,
    )
    #businesshours: List["BusinessHour"] = Relationship(back_populates="persons", link_model=PersonBusinessHoursLink)

    person_notes: List["Note"] = Relationship(
        link_model=PersonNotesLink,
    )
    events: List["Event"] = Relationship(
        back_populates="people",
        link_model=EventPeopleLink,
    )
    eventservices: List["EventService"] = Relationship(
        back_populates="associated_people",
        link_model=EventServicePeopleLink,
    )


class ArrangementType(SQLModel, TimeStampMixin, CamelCaseMixin, table=True):
    __tablename__ = "arrangement_arrangementtype"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=255)
    name_en: str = Field(max_length=255, nullable=True, default="")

    arrangements: List["Arrangement"] = Relationship(back_populates="arrangement_type")


class Arrangement(SQLModel, TimeStampMixin, CamelCaseMixin, table=True):
    __tablename__ = "arrangement_arrangement"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=255)
    name_en: str = Field(max_length=255, nullable=True, default="")
    stages: str = Field(default=StageChoices.PLANNING)
    starts: datetime.date
    ends: datetime.date

    arrangement_type_id: Optional[int] = Field(default=None, foreign_key="arrangement_arrangementtype.id")
    audience_id: Optional[int] = Field(default=None, foreign_key="arrangement_audience.id")
    responsible_id: Optional[int] = Field(default=None, foreign_key="arrangement_person.id")

    arrangement_type: Optional[ArrangementType] = Relationship(back_populates="arrangements")
    audience: Optional[Audience] = Relationship(back_populates="arrangements")
    responsible: Optional[Person] = Relationship(back_populates="arrangements")
    looseservicerequisitions: List["LooseServiceRequisition"] = Relationship(back_populates="arrangement")
    eventseries: List["EventSerie"] = Relationship(back_populates="arrangement")
    events: List["Event"] = Relationship(back_populates="arrangement")

    timeline_events: List["TimeLineEvent"] = Relationship(
        back_populates="arrangements",
        link_model=ArrangementTimelineEventsLink,
    )
    notes: List["Note"] = Relationship(
        back_populates="arrangement_notes",
        link_model=ArrangementNotesLink,
    )
    planners: List["Person"] = Relationship(
        back_populates="arrangement_planners",
        link_model=ArrangementOwnersLink,
    )
    people_participants: List["Person"] = Relationship(
        back_populates="arrangement_participants",
        link_model=ArrangementPeopleParticipantsLink,
    )
    organization_participants: List["Organization"] = Relationship(
        back_populates="arrangement_participants",
        link_model=ArrangementOrganizationParticipantsLink,
    )

    display_layouts: List["DisplayLayout"] = Relationship(
        link_model=ArrangementDisplayLayout,
    )


class Location(SQLModel, TimeStampMixin, CamelCaseMixin, table=True):
    __tablename__ = "arrangement_location"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    rooms: List["Room"] = Relationship(back_populates="location")

    #screen_resources: List["ScreenResource"] = Relationship(back_populates="location")


class Room(SQLModel, TimeStampMixin, CamelCaseMixin, table=True):
    __tablename__ = "arrangement_room"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    name_en: Optional[str]
    max_capacity: int = Field(alias="maxCapacity")
    has_screen: bool = Field(default=True)
    is_exclusive: bool = Field(default=False)
    location_id: Optional[int] = Field(foreign_key="arrangement_location.id", nullable=False)

    location: Optional[Location] = Relationship(back_populates="rooms")

    calendars: List["Calendar"] = Relationship(
        back_populates="room_resources",
        link_model=CalendarRoomLink,
    )
    events: List["Event"] = Relationship(
        back_populates="rooms",
        link_model=EventRoomLink,
    )


class RoomPreset(SQLModel, TimeStampMixin, CamelCaseMixin, table=True):
    __tablename__ = "arrangement_roompreset"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)

    rooms: List["Room"] = Relationship(
        link_model=RoomPresetLink,
    )


class Article(SQLModel, TimeStampMixin, CamelCaseMixin, table=True):
    __tablename__ = "arrangement_article"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=255)

    events: List["Event"] = Relationship(
        back_populates="articles",
        link_model=EventArticlesLink,
    )


class OrganizationType(SQLModel, TimeStampMixin, CamelCaseMixin, table=True):
    __tablename__ = "arrangement_organizationtype"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=255)

    organizations: List["Organization"] = Relationship(back_populates="organization_type")


class TimeLineEvent(SQLModel, TimeStampMixin, CamelCaseMixin, table=True):
    __tablename__ = "arrangement_timelineevent"

    id: Optional[int] = Field(default=None, primary_key=True)
    content: str = Field(max_length=1024)
    stamp: datetime.datetime = Field(nullable=False)

    arrangements: List["Arrangement"] = Relationship(
        back_populates="timeline_events",
        link_model=ArrangementTimelineEventsLink,
    )


class ServiceType(SQLModel, TimeStampMixin, CamelCaseMixin, table=True):
    __tablename__ = "arrangement_servicetype"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=255)

    serviceproviders: List["ServiceProvider"] = Relationship(back_populates="service_type")
    looseservicerequisitions: List["LooseServiceRequisition"] = Relationship(back_populates="type_to_order")


class ConfirmationReceipt(SQLModel, TimeStampMixin, CamelCaseMixin, table=True):
    __tablename__ = "arrangement_confirmationreceipt"
    __table_args__ = (UniqueConstraint("guid"),)

    id: Optional[int] = Field(default=None, primary_key=True)
    guid: str = Field(max_length=68, index=True)
    sent_to: str = Field(max_length=255)
    confirmed: bool = Field(default=False)
    sent_when: datetime.datetime = Field(default=None, nullable=True)
    confirmed_when: datetime.datetime = Field(default=None, nullable=True)
    requested_by_id: Optional[int] = Field(default=None, foreign_key="arrangement_person.id")
    note_id: Optional[int] = Field(foreign_key="arrangement_note.id", nullable=False)

    requested_by: Optional[Person] = Relationship(back_populates="confirmationreceipts")
    note: Optional["Note"] = Relationship(back_populates="reciept_notes")
    eventservices: List["EventService"] = Relationship(back_populates="receipt")


class Note(SQLModel, TimeStampMixin, CamelCaseMixin, table=True):
    __tablename__ = "arrangement_note"

    id: Optional[int] = Field(default=None, primary_key=True)
    content: str = Field(max_length=1024)

    author_id: Optional[int] = Field(foreign_key="arrangement_person.id", nullable=False)
    author: Optional[Person] = Relationship(back_populates="author_notes")

    reciept_notes: List["ConfirmationReceipt"] = Relationship(back_populates="note")

    persons: List["Person"] = Relationship(
        link_model=PersonNotesLink,
    ),

    arrangement_notes: List["Arrangement"] = Relationship(
        back_populates="notes",
        link_model=ArrangementNotesLink,
    )

    organization_notes: List["Organization"] = Relationship(
        back_populates="notes",
        link_model=OrganizationNotesLink,
    )

    events: List["Event"] = Relationship(
        back_populates="notes",
        link_model=EventNotesLink,
    )
    eventservices: List["EventService"] = Relationship(
        back_populates="notes",
        link_model=EventServiceNotesLink,
    )


class Organization(SQLModel, TimeStampMixin, CamelCaseMixin, table=True):
    __tablename__ = "arrangement_organization"

    id: Optional[int] = Field(default=None, primary_key=True)
    organization_number: int = Field(default=None, nullable=True)
    name: str = Field(max_length=255)

    organization_type_id: Optional[int] = Field(foreign_key="arrangement_organizationtype.id")

    organization_type: Optional[OrganizationType] = Relationship(back_populates="organizations")

    serviceproviders: List["ServiceProvider"] = Relationship(back_populates="organization")

    arrangement_participants: List["Arrangement"] = Relationship(
        back_populates="organization_participants",
        link_model=ArrangementOrganizationParticipantsLink,
    )

    members: List["Person"] = Relationship(
        back_populates="organization_members",
        link_model=OrganizationMembersLink,
    )

    notes: List["Note"] = Relationship(
        back_populates="organization_notes",
        link_model=OrganizationNotesLink,
    )


class Calendar(SQLModel, TimeStampMixin, CamelCaseMixin, table=True):
    __tablename__ = "arrangement_calendar"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=255)
    is_personal: bool = Field(default=True)

    owner_id: Optional[int] = Field(foreign_key="arrangement_person.id", nullable=False)

    owner: Optional[Person] = Relationship(back_populates="calendar_owners")

    people_resources: List["Person"] = Relationship(
        back_populates="calendars",
        link_model=CalendarPeopleLink,
    )

    room_resources: List["Room"] = Relationship(
        back_populates="calendars",
        link_model=CalendarRoomLink,
    )


class ServiceProvider(SQLModel, TimeStampMixin, CamelCaseMixin, table=True):
    __tablename__ = "arrangement_serviceprovider"

    id: Optional[int] = Field(default=None, primary_key=True)
    service_name: str = Field(max_length=255)

    service_type_id: Optional[int] = Field(foreign_key="arrangement_servicetype.id")
    organization_id: Optional[int] = Field(foreign_key="arrangement_organization.id")

    service_type: Optional[ServiceType] = Relationship(back_populates="serviceproviders")
    organization: Optional[Organization] = Relationship(back_populates="serviceproviders")
    eventservices: List["EventService"] = Relationship(back_populates="service_provider")


class EventSerie(SQLModel, TimeStampMixin, CamelCaseMixin, table=True):
    __tablename__ = "arrangement_eventserie"

    id: Optional[int] = Field(default=None, primary_key=True)
    arrangement_id: Optional[int] = Field(foreign_key="arrangement_arrangement.id")

    arrangement: Optional[Arrangement] = Relationship(back_populates="eventseries")

    events: List["Event"] = Relationship(back_populates="serie")


class Event(SQLModel, TimeStampMixin, CamelCaseMixin, table=True):
    __tablename__ = "arrangement_event"

    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(max_length=255)
    start: datetime.datetime = Field(nullable=False)
    end: datetime.datetime = Field(nullable=False)
    all_day: bool = Field(default=False)
    sequence_guid: str = Field(max_length=40, nullable=True)
    color: str = Field(max_length=40, nullable=True)

    serie_id: Optional[int] = Field(foreign_key="arrangement_eventserie.id", nullable=True, default=None)
    arrangement_id: Optional[int] = Field(foreign_key="arrangement_arrangement.id")

    serie: Optional[EventSerie] = Relationship(back_populates="events")
    arrangement: Optional[Arrangement] = Relationship(back_populates="events")
    eventservices: List["EventService"] = Relationship(back_populates="event")

    people: List["Person"] = Relationship(
        back_populates="events",
        link_model=EventPeopleLink,
    )
    rooms: List["Room"] = Relationship(
        back_populates="events",
        link_model=EventRoomLink,
    )
    loose_requisitions: List["LooseServiceRequisition"] = Relationship(
        back_populates="events",
        link_model=EventLooseServiceRequisitionLink,
    )

    articles: List["Article"] = Relationship(
        back_populates="events",
        link_model=EventArticlesLink,
    )
    """
    
    articles = relationship('Article', secondary=EventArticlesLink)
    """
   
    notes: List["Note"] = Relationship(
        back_populates="events",
        link_model=EventNotesLink,
    )

    display_layouts: List["DisplayLayout"] = Relationship(link_model=EventDisplayLayout)


class ScreenResourceGroup(SQLModel, TimeStampMixin, CamelCaseMixin, table=True):
    __tablename__ = "screenshow_screengroup_screens"

    id: Optional[int] = Field(default=None, primary_key=True)
    screengroup_id: Optional[int] = Field(foreign_key="screenshow_screengroup.id", nullable=False)
    screenresource_id: Optional[int] = Field(foreign_key="screenshow_screenresource.id", nullable=False)


class ScreenResource(SQLModel, TimeStampMixin, CamelCaseMixin, table=True):
    __tablename__ = "screenshow_screenresource"
    #__table_args__ = (UniqueConstraint("location_id", "name", name="uniq_name_loc_1"),)

    id: Optional[int] = Field(default=None, primary_key=True)
    screen_model: str = Field(max_length=255)
    items_shown: int = Field(default=10, nullable=False, description="Number of items to list on screen")
    room_id: Optional[int] = Field(foreign_key="arrangement_room.id", nullable=True)
    room: Optional["Room"] = Relationship()

    groups: List["ScreenGroup"] = Relationship(
        link_model=ScreenResourceGroup,
    )


class ScreenGroup(SQLModel, TimeStampMixin, CamelCaseMixin, table=True):
    __tablename__ = "screenshow_screengroup"

    id: Optional[int] = Field(default=None, primary_key=True)
    group_name: str = Field(max_length=255)
    group_name_en: str = Field(max_length=255, nullable=True)
    quantity: int = Field(default=10, nullable=False, description="Number of items to list on screen")
    #roompreset_id = Optional[int] = Field(foreign_key="arrangement_roompreset.id", nullable=True)

    #roompreset: Optional["RoomPreset"] = Relationship()

    screens: List["ScreenResource"] = Relationship(
        link_model=ScreenResourceGroup,
    )


class DisplayLayoutResource(SQLModel, table=True):
    __tablename__ = "screenshow_displaylayout_screens"

    id: Optional[int] = Field(default=None, primary_key=True)
    displaylayout_id: Optional[int] = Field(foreign_key="screenshow_displaylayout.id", nullable=False)
    screenresource_id: Optional[int] = Field(foreign_key="screenshow_screenresource.id", nullable=True)


class DisplayLayoutGroup(SQLModel, table=True):
    __tablename__ = "screenshow_displaylayout_groups"

    id: Optional[int] = Field(default=None, primary_key=True)
    displaylayout_id: Optional[int] = Field(foreign_key="screenshow_displaylayout.id", nullable=False)
    screengroup_id: Optional[int] = Field(foreign_key="screenshow_screengroup.id", nullable=True)


class DisplayLayout(SQLModel, TimeStampMixin, CamelCaseMixin, table=True):
    __tablename__ = "screenshow_displaylayout"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=255)
    description: str = Field(max_length=1024)
    items_shown: int = Field(default=10, nullable=False, description="Number of items to list on screen")
    is_room_based: bool = Field(default=True, nullable=False, description="If true app will create events per room")
    all_events: bool = Field(default=True, nullable=False, description="Showing all events")
    is_active: bool = Field(default=True, description="Is Layout Active")
    setting_id: Optional[int] = Field(foreign_key="screenshow_displaylayoutsetting.id", nullable=True)

    setting: Optional["DisplayLayoutSetting"] = Relationship(back_populates="layouts")

    screens: List["ScreenResource"] = Relationship(
        link_model=DisplayLayoutResource,
    )
    groups: List["ScreenGroup"] = Relationship(
        link_model=DisplayLayoutGroup,
    )


class DisplayLayoutSetting(SQLModel, TimeStampMixin, CamelCaseMixin, table=True):
    __tablename__ = "screenshow_displaylayoutsetting"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=255)
    html_template: Optional[str]
    css_template: Optional[str]
    file_output_path: str

    layouts: List["DisplayLayout"] = Relationship(back_populates="setting")


class EventService(SQLModel, TimeStampMixin, CamelCaseMixin, table=True):
    __tablename__ = "arrangement_eventservice"

    id: Optional[int] = Field(default=None, primary_key=True)

    receipt_id: Optional[int] = Field(foreign_key="arrangement_confirmationreceipt.id")
    event_id: Optional[int] = Field(foreign_key="arrangement_event.id")
    service_provider_id: Optional[int] = Field(foreign_key="arrangement_serviceprovider.id")

    receipt: Optional[ConfirmationReceipt] = Relationship(back_populates="eventservices")
    event: Optional[Event] = Relationship(back_populates="eventservices")
    service_provider: Optional[ServiceProvider] = Relationship(back_populates="eventservices")

    notes: List["Note"] = Relationship(
        back_populates="eventservices",
        link_model=EventServiceNotesLink,
    )
    associated_people: List["Person"] = Relationship(
        back_populates="eventservices",
        link_model=EventServicePeopleLink,
    )




class LooseServiceRequisition(SQLModel, TimeStampMixin, CamelCaseMixin, table=True):
    __tablename__ = "arrangement_looseservicerequisition"

    id: Optional[int] = Field(default=None, primary_key=True)
    comment: str = Field(default='')

    arrangement_id: Optional[int] = Field(foreign_key="arrangement_arrangement.id")
    type_to_order_id: Optional[int] = Field(foreign_key="arrangement_servicetype.id")

    arrangement: Optional[Arrangement] = Relationship(back_populates="looseservicerequisitions")
    type_to_order: Optional[ServiceType] = Relationship(back_populates="looseservicerequisitions")

    events: List["Event"] = Relationship(back_populates="loose_requisitions",
                                                                       link_model=EventLooseServiceRequisitionLink)
