from typing import Optional
from sqlmodel import Field, SQLModel


class LocationBase(SQLModel):
    name: str = Field(index=True)


class Location(LocationBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)