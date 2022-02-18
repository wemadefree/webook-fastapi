from typing import List, Optional
from sqlmodel import Field, SQLModel
from app.arrangement.models import LocationBase, RoomBase


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


class RoomUpdate(SQLModel):
    name: Optional[str] = None


class RoomReadWithLocation(RoomRead):
    location: Optional[LocationRead] = None


class LocationReadWithRoom(LocationRead):
    rooms: List[RoomRead] = []