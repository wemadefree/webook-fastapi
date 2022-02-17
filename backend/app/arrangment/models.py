from typing import List, Optional
from sqlmodel import Field, Relationship, SQLModel


class LocationBase(SQLModel):
    name: str = Field(index=True)


class Location(LocationBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    rooms: List["Room"] = Relationship(back_populates="location")


class RoomBase(SQLModel):
    name: str = Field(index=True)
    location_id: Optional[int] = Field(default=None, foreign_key="location.id")


class Room(RoomBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    location: Optional[Location] = Relationship(back_populates="rooms")