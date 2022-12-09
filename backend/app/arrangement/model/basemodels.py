from typing import List, Optional

from app.arrangement.model.linkmodels import (
    ArrangementDisplayLayout,
    ArrangementOrganizationParticipantsLink,
    ArrangementOwnersLink,
    ArrangementPeopleParticipantsLink,
    DisplayLayoutGroup,
    DisplayLayoutResource,
    EventArticlesLink,
    EventDisplayLayout,
    EventPeopleLink,
    EventRoomLink,
    OrganizationMembersLink,
    RoomPresetLink,
    ScreenResourceGroup,
)
from app.core.mixins import (
    ArchivedMixin,
    CamelModelMixin,
    SlugifyNameMixin,
    TimeStampMixin,
)
from app.core.session import Base
from slugify import slugify
from sqlalchemy import Boolean, Column, Date, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, validates


class StageChoices:
    PLANNING = "planning"
    REQUISITIONING = "requisitioning"
    READY_TO_LAUNCH = "ready_to_launch"
    IN_PRODUCTION = "in_production"


class ScreenStatus:
    AVAILABLE = 0
    UNAVAILABLE = 1


class Audience(Base, TimeStampMixin, SlugifyNameMixin):
    __tablename__ = "arrangement_audience"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    name_en = Column(String, nullable=True)
    icon_class = Column(String, nullable=True)

    parent_id = Column(Integer, ForeignKey("arrangement_audience.id"))
    parent = relationship("Audience", remote_side=[id])

    arrangements = relationship("Arrangement", back_populates="audience")


class Person(SlugifyNameMixin, Base, TimeStampMixin, ArchivedMixin):
    __tablename__ = "arrangement_person"

    id = Column(Integer, primary_key=True, index=True)

    social_provider_id = Column(String, nullable=True)
    social_provider_email = Column(String, nullable=True)

    personal_email = Column(String, nullable=True)
    first_name = Column(String)
    middle_name = Column(String)
    last_name = Column(String)
    birth_date = Column(Date, nullable=True)

    organizations = relationship(
        "Organization",
        secondary="arrangement_organization_members",
        back_populates="members",
    )
    arrangement_participants = relationship(
        "Arrangement",
        secondary="arrangement_arrangement_people_participants",
        back_populates="people_participants",
    )
    arrangement_planners = relationship(
        "Arrangement",
        secondary="arrangement_arrangement_planners",
        back_populates="planners",
    )
    arrangement_responsibles = relationship("Arrangement", back_populates="responsible")
    events = relationship(
        "Event", secondary="arrangement_event_people", back_populates="people"
    )


class ArrangementType(Base, TimeStampMixin, SlugifyNameMixin):
    __tablename__ = "arrangement_arrangementtype"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    name_en = Column(String, nullable=True)

    parent_id = Column(Integer, ForeignKey("arrangement_arrangementtype.id"))
    parent = relationship("ArrangementType", remote_side=[id])

    arrangements = relationship("Arrangement", back_populates="arrangement_type")


class Arrangement(Base, TimeStampMixin, SlugifyNameMixin):
    __tablename__ = "arrangement_arrangement"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    name_en = Column(String, nullable=True)
    stages = Column(String, index=True, nullable=False, default=StageChoices.PLANNING)
    starts = Column(DateTime, nullable=True)
    ends = Column(DateTime, nullable=True)
    meeting_place = Column(String, nullable=True)
    meeting_place_en = Column(String, nullable=True)

    location_id = Column(Integer, ForeignKey("arrangement_location.id"), nullable=False)
    location = relationship("Location", back_populates="arrangements")

    audience_id = Column(Integer, ForeignKey("arrangement_audience.id"), nullable=False)
    audience = relationship("Audience", back_populates="arrangements")

    arrangement_type_id = Column(
        Integer, ForeignKey("arrangement_arrangementtype.id"), nullable=False
    )
    arrangement_type = relationship("ArrangementType", back_populates="arrangements")

    responsible_id = Column(
        Integer, ForeignKey("arrangement_person.id"), nullable=False
    )
    responsible = relationship("Person", back_populates="arrangement_responsibles")

    events = relationship("Event", back_populates="arrangement")
    organization_participants = relationship(
        "Organization",
        secondary="arrangement_arrangement_organization_participants",
        back_populates="arrangements",
    )
    people_participants = relationship(
        "Person",
        secondary="arrangement_arrangement_people_participants",
        back_populates="arrangement_participants",
    )
    planners = relationship(
        "Person",
        secondary="arrangement_arrangement_planners",
        back_populates="arrangement_planners",
    )
    display_layouts = relationship(
        "DisplayLayout",
        secondary="arrangement_arrangement_display_layouts",
        back_populates="arrangements",
    )


class Location(Base, TimeStampMixin, SlugifyNameMixin):
    __tablename__ = "arrangement_location"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)

    rooms = relationship("Room", back_populates="location")
    arrangements = relationship("Arrangement", back_populates="location")

    is_archived = Column(Boolean, default=False)


class Room(Base, TimeStampMixin, SlugifyNameMixin):
    __tablename__ = "arrangement_room"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    name_en = Column(String, nullable=True)
    max_capacity = Column(Integer, default=10, nullable=False)
    has_screen = Column(Boolean, default=True)
    is_exclusive = Column(Boolean, default=False)

    location_id = Column(Integer, ForeignKey("arrangement_location.id"), nullable=False)
    location = relationship("Location", back_populates="rooms")

    events = relationship(
        "Event", secondary="arrangement_event_rooms", back_populates="rooms"
    )


class RoomPreset(Base, TimeStampMixin, SlugifyNameMixin):
    __tablename__ = "arrangement_roompreset"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)

    rooms = relationship("Room", secondary="arrangement_roompreset_rooms")


class Article(Base, TimeStampMixin, SlugifyNameMixin):
    __tablename__ = "arrangement_article"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)


class OrganizationType(Base, TimeStampMixin, SlugifyNameMixin):
    __tablename__ = "arrangement_organizationtype"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)

    organizations = relationship("Organization", back_populates="organization_type")


class Organization(Base, TimeStampMixin, SlugifyNameMixin):
    __tablename__ = "arrangement_organization"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    organization_number = Column(Integer, default=None, nullable=True)

    organization_type_id = Column(
        Integer, ForeignKey("arrangement_organizationtype.id"), nullable=False
    )
    organization_type = relationship("OrganizationType", back_populates="organizations")

    arrangements = relationship(
        "Arrangement",
        secondary="arrangement_arrangement_organization_participants",
        back_populates="organization_participants",
    )
    members = relationship(
        "Person",
        secondary="arrangement_organization_members",
        back_populates="organizations",
    )


class Event(Base, TimeStampMixin):
    __tablename__ = "arrangement_event"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=True)
    title_en = Column(String, nullable=True)
    start = Column(DateTime, nullable=True)
    end = Column(DateTime, nullable=True)
    all_day = Column(Boolean, default=False)
    sequence_guid = Column(String, nullable=True)
    is_archived = Column(Boolean, default=False)
    display_text = Column(String, nullable=True)
    display_text_en = Column(String, nullable=True)
    meeting_place = Column(String)
    meeting_place_en = Column(String)

    arrangement_type_id = Column(Integer, ForeignKey("arrangement_arrangementtype.id"))
    arrangement_type = relationship("ArrangementType")

    audience_id = Column(Integer, ForeignKey("arrangement_audience.id"))
    audience = relationship("Audience")

    arrangement_id = Column(
        Integer,
        ForeignKey("arrangement_arrangement.id"),
    )
    arrangement = relationship("Arrangement", back_populates="events")

    display_layouts = relationship(
        "DisplayLayout",
        secondary="arrangement_event_display_layouts",
        back_populates="events",
    )

    articles = relationship("Article", secondary="arrangement_event_articles")
    rooms = relationship(
        "Room", secondary="arrangement_event_rooms", back_populates="events"
    )
    people = relationship(
        "Person", secondary="arrangement_event_people", back_populates="events"
    )


class ScreenResource(Base, TimeStampMixin):
    __tablename__ = "screenshow_screenresource"

    id = Column(Integer, primary_key=True, index=True)
    screen_model = Column(String, nullable=False)
    items_shown = Column(Integer, default=10, nullable=False)
    status = Column(Integer, default=ScreenStatus.UNAVAILABLE)

    room_id = Column(
        Integer,
        ForeignKey("arrangement_room.id"),
    )
    room = relationship("Room")

    display_layouts = relationship(
        "DisplayLayout",
        secondary="screenshow_displaylayout_screens",
        back_populates="screens",
    )
    slug = Column(String(100), nullable=False)

    @validates("screen_model")
    def create_slug_by_name(self, key, value):
        self.slug = slugify(value)
        return value


class ScreenGroup(Base, TimeStampMixin):
    __tablename__ = "screenshow_screengroup"

    id = Column(Integer, primary_key=True, index=True)
    group_name = Column(String, nullable=False)
    group_name_en = Column(String, nullable=True)
    quantity = Column(Integer, default=10, nullable=False)

    display_layouts = relationship(
        "DisplayLayout",
        secondary="screenshow_displaylayout_groups",
        back_populates="groups",
    )
    screens = relationship(
        "ScreenResource",
        secondary="screenshow_screengroup_screens",
    )


class DisplayLayout(Base, TimeStampMixin, SlugifyNameMixin):
    __tablename__ = "screenshow_displaylayout"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    items_shown = Column(Integer, default=10, nullable=False)
    is_room_based = Column(Boolean, default=True)
    all_events = Column(Boolean, default=True)
    is_active = Column(Boolean, default=True)

    setting_id = Column(
        Integer,
        ForeignKey("screenshow_displaylayoutsetting.id"),
    )
    setting = relationship("DisplayLayoutSetting", back_populates="layouts")

    arrangements = relationship(
        "Arrangement",
        secondary="arrangement_arrangement_display_layouts",
        back_populates="display_layouts",
    )
    events = relationship(
        "Event",
        secondary="arrangement_event_display_layouts",
        back_populates="display_layouts",
    )
    screens = relationship(
        "ScreenResource",
        secondary="screenshow_displaylayout_screens",
        back_populates="display_layouts",
    )
    groups = relationship(
        "ScreenGroup",
        secondary="screenshow_displaylayout_groups",
        back_populates="display_layouts",
    )


class DisplayLayoutSetting(Base):
    __tablename__ = "screenshow_displaylayoutsetting"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    html_template = Column(String, nullable=True)
    css_template = Column(String, nullable=True)
    file_output_path = Column(String, nullable=True)

    layouts = relationship("DisplayLayout", back_populates="setting")
