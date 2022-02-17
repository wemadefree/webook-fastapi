from typing import Optional
from sqlmodel import Field, SQLModel
from .models import LocationBase, Location


class LocationCreate(LocationBase):
    pass


class LocationRead(LocationBase):
    id: int


class LocationUpdate(SQLModel):
    name: Optional[str] = None