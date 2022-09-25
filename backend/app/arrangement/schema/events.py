import datetime
from typing import List, Optional

from app.arrangement.schema.arrangements import (
    ArrangementRead, ArrangementDisplayRead, ArrangementTypeBase, AudienceRead
)
from app.arrangement.schema.html_generator import DisplayLayoutSimple
from app.arrangement.schema.persons import PersonRead
from app.arrangement.schema.rooms import RoomRead, RoomWithLocation
from app.core.mixins import CamelModelMixin


class ArticleBase(CamelModelMixin):
    name: str

    class Config:
        orm_mode = True


class ArticleRead(ArticleBase):
    id: int


class ArticleCreate(ArticleBase):
    pass


class ArticleUpdate(CamelModelMixin):
    name: Optional[str]

    class Config:
        orm_mode = True


class ArticleAddOrUpdate(ArticleUpdate):
    id: int


class EventBase(CamelModelMixin):
    title: str
    title_en: Optional[str]
    start: datetime.datetime
    end: datetime.datetime
    all_day: bool
    sequence_guid: Optional[str]
    display_text: Optional[str]
    display_text_en: Optional[str]
    serie_id: Optional[int]
    arrangement_id: Optional[int]
    arrangement_type_id: Optional[int]
    audience_id: Optional[int]

    class Config:
        orm_mode = True


class EventCreate(EventBase):
    pass


class EventRead(EventBase):
    id: int
    display_layouts: List[DisplayLayoutSimple]


class EventUpdate(CamelModelMixin):
    title: Optional[str]
    title_en: Optional[str]
    start: Optional[datetime.datetime]
    end: Optional[datetime.datetime]
    all_day: Optional[bool]
    sequence_guid: Optional[str]
    display_text: Optional[str]
    display_text_en: Optional[str]
    serie_id: Optional[int]
    arrangement_id: Optional[int]
    arrangement_type_id: Optional[int]
    audience_id: Optional[int]

    class Config:
        orm_mode = True


class EventReadExtra(EventRead):
    arrangement: Optional[ArrangementRead]
    people: List[PersonRead]
    rooms: List[RoomRead]
    articles: List[ArticleRead]
    arrangement_type: Optional[ArrangementTypeBase]
    audience:  Optional[AudienceRead]


class EventDisplayRead(CamelModelMixin):
    id: int
    title: str
    title_en: Optional[str]
    start: datetime.datetime
    end: datetime.datetime
    all_day: bool
    arrangement: ArrangementDisplayRead
    arrangement_type: Optional[ArrangementTypeBase]
    audience: Optional[AudienceRead]
    display_text: Optional[str]
    display_text_en: Optional[str]
    rooms: List[RoomWithLocation]
    display_layouts: List[DisplayLayoutSimple]

    class Config:
        orm_mode = True







