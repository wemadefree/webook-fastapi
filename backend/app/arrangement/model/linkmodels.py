from typing import Optional
from sqlmodel import Field, SQLModel


class ArrangementOwnersLink(SQLModel, table=True):
    __tablename__ = "arrangement_arrangement_planners"

    id: Optional[int] = Field(default=None, primary_key=True)
    arrangement_id: Optional[int] = Field(foreign_key="arrangement_arrangement.id", nullable=False)
    person_id: Optional[int] = Field(foreign_key="arrangement_person.id", nullable=False)


class ArrangementDisplayLayout(SQLModel, table=True):
    __tablename__ = "arrangement_arrangement_display_layouts"

    id: Optional[int] = Field(default=None, primary_key=True)
    displaylayout_id: Optional[int] = Field(foreign_key="screenshow_displaylayout.id", nullable=False)
    arrangement_id: Optional[int] = Field(foreign_key="arrangement_arrangement.id", nullable=False)


class ArrangementPeopleParticipantsLink(SQLModel, table=True):
    __tablename__ = "arrangement_arrangement_people_participants"

    id: Optional[int] = Field(default=None, primary_key=True)
    arrangement_id: Optional[int] = Field(foreign_key="arrangement_arrangement.id", nullable=False)
    person_id: Optional[int] = Field(foreign_key="arrangement_person.id", nullable=False)


class ArrangementOrganizationParticipantsLink(SQLModel, table=True):
    __tablename__ = "arrangement_arrangement_organization_participants"

    id: Optional[int] = Field(default=None, primary_key=True)
    arrangement_id: Optional[int] = Field(foreign_key="arrangement_arrangement.id", nullable=False)
    organization_id: Optional[int] = Field(foreign_key="arrangement_organization.id", nullable=False)


class ArrangementTimelineEventsLink(SQLModel, table=True):
    __tablename__ = "arrangement_arrangement_timeline_events"

    id: Optional[int] = Field(default=None, primary_key=True)
    arrangement_id: Optional[int] = Field(foreign_key="arrangement_arrangement.id", nullable=False)
    timelineevent_id: Optional[int] = Field(foreign_key="arrangement_timelineevent.id", nullable=False)


class CalendarPeopleLink(SQLModel, table=True):
    __tablename__ = "arrangement_calendar_people_resources"

    id: Optional[int] = Field(default=None, primary_key=True)
    calendar_id: Optional[int] = Field(foreign_key="arrangement_calendar.id", nullable=False)
    person_id: Optional[int] = Field(foreign_key="arrangement_person.id", nullable=False)


class CalendarRoomLink(SQLModel, table=True):
    __tablename__ = "arrangement_calendar_room_resources"

    id: Optional[int] = Field(default=None, primary_key=True)
    calendar_id: Optional[int] = Field(foreign_key="arrangement_calendar.id", nullable=False)
    room_id: Optional[int] = Field(foreign_key="arrangement_room.id", nullable=False)


class EventDisplayLayout(SQLModel, table=True):
    __tablename__ = "arrangement_event_display_layouts"

    id: Optional[int] = Field(default=None, primary_key=True)
    displaylayout_id: Optional[int] = Field(foreign_key="screenshow_displaylayout.id", nullable=False)
    event_id: Optional[int] = Field(foreign_key="arrangement_event.id", nullable=False)


class EventArticlesLink(SQLModel, table=True):
    __tablename__ = "arrangement_event_articles"

    id: Optional[int] = Field(default=None, primary_key=True)
    event_id: Optional[int] = Field(foreign_key="arrangement_event.id", nullable=False)
    article_id: Optional[int] = Field(foreign_key="arrangement_article.id", nullable=False)


class EventNotesLink(SQLModel, table=True):
    __tablename__ = "arrangement_event_notes"

    id: Optional[int] = Field(default=None, primary_key=True)
    event_id: Optional[int] = Field(foreign_key="arrangement_event.id", nullable=False)
    note_id: Optional[int] = Field(foreign_key="arrangement_note.id", nullable=False)


class EventPeopleLink(SQLModel, table=True):
    __tablename__ = "arrangement_event_people"

    id: Optional[int] = Field(default=None, primary_key=True)
    event_id: Optional[int] = Field(foreign_key="arrangement_event.id", nullable=False)
    person_id: Optional[int] = Field(foreign_key="arrangement_person.id", nullable=False)


class EventRoomLink(SQLModel, table=True):
    __tablename__ = "arrangement_event_rooms"

    id: Optional[int] = Field(default=None, primary_key=True)
    event_id: Optional[int] = Field(foreign_key="arrangement_event.id", nullable=False)
    room_id: Optional[int] = Field(foreign_key="arrangement_room.id", nullable=False)


class EventServicePeopleLink(SQLModel, table=True):
    __tablename__ = "arrangement_eventservice_associated_people"

    id: Optional[int] = Field(default=None, primary_key=True)
    eventservice_id: Optional[int] = Field(foreign_key="arrangement_eventservice.id", nullable=False)
    person_id: Optional[int] = Field(foreign_key="arrangement_person.id", nullable=False)


class EventServiceNotesLink(SQLModel, table=True):
    __tablename__ = "arrangement_eventservice_notes"

    id: Optional[int] = Field(default=None, primary_key=True)
    eventservice_id: Optional[int] = Field(foreign_key="arrangement_eventservice.id", nullable=False)
    note_id: Optional[int] = Field(foreign_key="arrangement_note.id", nullable=False)


class OrganizationMembersLink(SQLModel, table=True):
    __tablename__ = "arrangement_organization_members"

    id: Optional[int] = Field(default=None, primary_key=True)
    organization_id: Optional[int] = Field(foreign_key="arrangement_organization.id", nullable=False)
    person_id: Optional[int] = Field(foreign_key="arrangement_person.id", nullable=False)


class OrganizationNotesLink(SQLModel, table=True):
    __tablename__ = "arrangement_organization_notes"

    id: Optional[int] = Field(default=None, primary_key=True)
    organization_id: Optional[int] = Field(foreign_key="arrangement_organization.id", nullable=False)
    note_id: Optional[int] = Field(foreign_key="arrangement_note.id", nullable=False)


class EventLooseServiceRequisitionLink(SQLModel, table=True):
    __tablename__ = "arrangement_event_loose_requisitions"

    id: Optional[int] = Field(default=None, primary_key=True)
    event_id: Optional[int] = Field(foreign_key="arrangement_event.id", nullable=False)
    looseservicerequisition_id: Optional[int] = Field(foreign_key="arrangement_looseservicerequisition.id", nullable=False)


class ArrangementNotesLink(SQLModel, table=True):
    __tablename__ = "arrangement_arrangement_notes"

    id: Optional[int] = Field(default=None, primary_key=True)
    note_id: Optional[int] = Field(foreign_key="arrangement_note.id", nullable=False)
    arrangement_id: Optional[int] = Field(foreign_key="arrangement_arrangement.id", nullable=False)

"""
class PersonBusinessHoursLink(SQLModel, table=True):
    __tablename__ = "arrangement_person_business_hour"

    id: Optional[int] = Field(default=None, primary_key=True)
    businesshour_id: Optional[int] = Field(foreign_key="arrangement_businesshour.id", nullable=False)
    person_id: Optional[int] = Field(foreign_key="arrangement_person.id", nullable=False)
"""

class PersonNotesLink(SQLModel, table=True):
    __tablename__ = "arrangement_person_notes"

    id: Optional[int] = Field(default=None, primary_key=True)
    note_id: Optional[int] = Field(foreign_key="arrangement_note.id", nullable=False)
    person_id: Optional[int] = Field(foreign_key="arrangement_person.id", nullable=False)

class RoomPresetLink(SQLModel, table=True):
    __tablename__ = "arrangement_roompreset_rooms"

    id: Optional[int] = Field(default=None, primary_key=True)
    roompreset_id: Optional[int] = Field(foreign_key="arrangement_roompreset.id", nullable=False)
    room_id: Optional[int] = Field(foreign_key="arrangement_room.id", nullable=False)
