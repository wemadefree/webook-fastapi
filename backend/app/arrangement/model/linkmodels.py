from typing import Optional
from sqlmodel import Field, SQLModel


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


class ArrangementNotesLink(SQLModel, table=True):
    __tablename__ = "arrangement_notes"

    id: Optional[int] = Field(default=None, primary_key=True)
    note_id: Optional[int] = Field(foreign_key="note.id", nullable=False)
    arrangement_id: Optional[int] = Field(foreign_key="arrangement.id", nullable=False)


class PersonBusinessHoursLink(SQLModel, table=True):
    __tablename__ = "person_business_hour"

    id: Optional[int] = Field(default=None, primary_key=True)
    businesshour_id: Optional[int] = Field(foreign_key="businesshour.id", nullable=False)
    person_id: Optional[int] = Field(foreign_key="person.id", nullable=False)


class PersonNotesLink(SQLModel, table=True):
    __tablename__ = "person_notes"

    id: Optional[int] = Field(default=None, primary_key=True)
    note_id: Optional[int] = Field(foreign_key="note.id", nullable=False)
    person_id: Optional[int] = Field(foreign_key="person.id", nullable=False)