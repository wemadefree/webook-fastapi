from typing import List, Optional

from app.core.mixins import CamelModelMixin


class LocationBase(CamelModelMixin):
    name: str

    class Config:
        orm_mode = True


class LocationCreate(LocationBase):
    pass


class LocationRead(LocationBase):
    id: int


class LocationUpdate(CamelModelMixin):
    name: Optional[str] = None

    class Config:
        orm_mode = True


class RoomBase(CamelModelMixin):
    name: str
    name_en: Optional[str]
    max_capacity: int
    is_exclusive: bool
    has_screen: bool
    location_id: Optional[int]

    class Config:
        orm_mode = True


class RoomCreate(RoomBase):
    pass


class RoomRead(RoomBase):
    id: int


class RoomUpdate(CamelModelMixin):
    name: Optional[str] = None
    name_en: Optional[str]
    max_capacity: Optional[int]
    is_exclusive: Optional[bool]
    location_id: Optional[int]
    has_screen: Optional[bool]

    class Config:
        orm_mode = True


class RoomAddOrUpdate(CamelModelMixin):
    id: int
    name: Optional[str] = None
    name_en: Optional[str]
    max_capacity: Optional[int]
    is_exclusive: Optional[bool]
    has_screen: Optional[bool]
    location_id: Optional[int]


class RoomWithLocation(CamelModelMixin):
    id: int
    name: str
    name_en: Optional[str]
    max_capacity: int
    is_exclusive: bool
    has_screen: bool
    location: Optional[LocationRead]

    class Config:
        orm_mode = True


class LocationReadWithRoom(LocationRead):
    rooms: List[RoomRead] = []


class RoomPresetBase(CamelModelMixin):
    name: str

    class Config:
        orm_mode = True


class RoomPresetCreate(RoomPresetBase):
    pass


class RoomPresetRead(RoomPresetBase):
    id: int
    rooms: Optional[List[RoomRead]]


class RoomPresetUpdate(CamelModelMixin):
    name: Optional[str]

    class Config:
        orm_mode = True

