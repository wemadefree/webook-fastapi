import datetime
from typing import List, Optional
from sqlalchemy import UniqueConstraint
from sqlmodel import Field, Relationship, SQLModel

from app.core.mixins import CamelCaseMixin, TimeStampMixin


class LocationBase(SQLModel, CamelCaseMixin):
    name: str = Field(index=True)


class Location(LocationBase, TimeStampMixin, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    rooms: List["Room"] = Relationship(back_populates="location")


class RoomBase(SQLModel, CamelCaseMixin):
    name: str = Field(index=True)
    max_capacity: int = Field(alias="maxCapacity")
    location_id: Optional[int] = Field(default=None, foreign_key="location.id")


class Room(RoomBase, TimeStampMixin, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    location: Optional[Location] = Relationship(back_populates="rooms")


class AudienceBase(SQLModel):
    name: str = Field(..., max_length=255)
    icon_class: Optional[str] = Field(default='',  max_length=255)


class ArrangementBase(SQLModel):
    name: str = Field(max_length=255)
    starts: datetime.date
    ends: datetime.date


class ArticleBase(SQLModel):
    name: str = Field(max_length=255)


class OrganizationTypeBase(SQLModel):
    name: str = Field(max_length=255)


class TimeLineBase(SQLModel):
    content: str = Field(max_length=1024)
    stamp: datetime.datetime


class ServiceType(SQLModel):
    name: str = Field(max_length=255)


class BusinessHour(SQLModel):
    start_of_business_hours: datetime.time
    end_of_business_hours: datetime.time


class NoteBase(SQLModel):
    content: str = Field(max_length=1024)


class ConfirmationReceiptBase(SQLModel):
    __table_args__ = (UniqueConstraint("guid"),)

    guid: str = Field(max_length=68, index=True)
    sent_to: str = Field(max_length=255)
    confirmed: bool = Field(default=False)
    sent_when: datetime.datetime = Field(default=None)
    confirmed_when: datetime.datetime = Field(default=None)


class PersonBase(SQLModel):
    __table_args__ = (UniqueConstraint("guid"),)

    personal_email: str = Field(max_length=255, nullable=False)
    first_name: str = Field(max_length=255)
    middle_name: str = Field(max_length=255)
    last_name: str = Field(max_length=255)
    birth_date: datetime.date = Field(nullable=False)
