from sqlalchemy import Column, Integer, ForeignKey
from typing import Optional

from app.core.session import Base


class ArrangementOwnersLink(Base):
    __tablename__ = "arrangement_arrangement_planners"

    id = Column(Integer, primary_key=True, index=True)
    arrangement_id = Column(Integer, ForeignKey("arrangement_arrangement.id"))
    person_id = Column(Integer, ForeignKey("arrangement_person.id"))


class ArrangementDisplayLayout(Base):
    __tablename__ = "arrangement_arrangement_display_layouts"

    id = Column(Integer, primary_key=True, index=True)
    arrangement_id = Column(Integer, ForeignKey("arrangement_arrangement.id"))
    displaylayout_id = Column(Integer, ForeignKey("screenshow_displaylayout.id"))


class ArrangementOrganizationParticipantsLink(Base):
    __tablename__ = "arrangement_arrangement_organization_participants"

    id = Column(Integer, primary_key=True, index=True)
    arrangement_id = Column(Integer, ForeignKey("arrangement_arrangement.id"))
    organization_id = Column(Integer, ForeignKey("arrangement_organization.id"))


class ArrangementPeopleParticipantsLink(Base):
    __tablename__ = "arrangement_arrangement_people_participants"

    id = Column(Integer, primary_key=True, index=True)
    arrangement_id = Column(Integer, ForeignKey("arrangement_arrangement.id"))
    person_id = Column(Integer, ForeignKey("arrangement_person.id"))


class DisplayLayoutResource(Base):
    __tablename__ = "screenshow_displaylayout_screens"

    id = Column(Integer, primary_key=True, index=True)
    displaylayout_id = Column(Integer, ForeignKey("screenshow_displaylayout.id"))
    screenresource_id = Column(Integer, ForeignKey("screenshow_screenresource.id"))


class DisplayLayoutGroup(Base):
    __tablename__ = "screenshow_displaylayout_groups"

    id = Column(Integer, primary_key=True, index=True)
    displaylayout_id = Column(Integer, ForeignKey("screenshow_displaylayout.id"))
    screengroup_id = Column(Integer, ForeignKey("screenshow_screengroup.id"))


class EventDisplayLayout(Base):
    __tablename__ = "arrangement_event_display_layouts"

    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey("arrangement_event.id"))
    displaylayout_id = Column(Integer, ForeignKey("screenshow_displaylayout.id"))


class EventArticlesLink(Base):
    __tablename__ = "arrangement_event_articles"

    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey("arrangement_event.id"))
    article_id = Column(Integer, ForeignKey("arrangement_article.id"))


class EventPeopleLink(Base):
    __tablename__ = "arrangement_event_people"

    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey("arrangement_event.id"))
    person_id = Column(Integer, ForeignKey("arrangement_person.id"))


class EventRoomLink(Base):
    __tablename__ = "arrangement_event_rooms"

    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey("arrangement_event.id"))
    room_id = Column(Integer, ForeignKey("arrangement_room.id"))


class OrganizationMembersLink(Base):
    __tablename__ = "arrangement_organization_members"

    id = Column(Integer, primary_key=True, index=True)
    organization_id = Column(Integer, ForeignKey("arrangement_organization.id"))
    person_id = Column(Integer, ForeignKey("arrangement_person.id"))


class RoomPresetLink(Base):
    __tablename__ = "arrangement_roompreset_rooms"

    id = Column(Integer, primary_key=True, index=True)
    roompreset_id = Column(Integer, ForeignKey("arrangement_roompreset.id"))
    room_id = Column(Integer, ForeignKey("arrangement_room.id"))


class ScreenResourceGroup(Base):
    __tablename__ = "screenshow_screengroup_screens"

    id = Column(Integer, primary_key=True, index=True)
    screenresource_id = Column(Integer, ForeignKey("screenshow_screenresource.id"))
    screengroup_id = Column(Integer, ForeignKey("screenshow_screengroup.id"))


