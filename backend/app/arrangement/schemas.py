from typing import List, Optional
from sqlmodel import Field, SQLModel
from app.core.mixins import CamelCaseMixin


class LocationBase(SQLModel, CamelCaseMixin):
    name: str = Field(index=True)


class LocationCreate(LocationBase):
    pass


class LocationRead(LocationBase):
    id: int


class LocationUpdate(SQLModel):
    name: Optional[str] = None


class RoomBase(SQLModel, CamelCaseMixin):
    name: str = Field(index=True)
    max_capacity: int = Field(alias="maxCapacity")
    location_id: Optional[int] = Field(default=None, foreign_key="location.id")


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
