from typing import List, Optional
from sqlmodel import SQLModel

from app.arrangement.models import LocationBase, RoomBase
from app.core.mixins import CamelCaseMixin


class LocationCreate(LocationBase):
    pass


class LocationRead(LocationBase):
    id: int


class LocationUpdate(SQLModel):
    name: Optional[str] = None


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
