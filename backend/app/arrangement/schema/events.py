import datetime
from typing import List, Literal, Optional

from app.arrangement.model.choicemodels import AssociationTypeChoice, EventTypeChoice
from app.arrangement.schema.arrangements import ArrangementRead, ArrangementDisplayRead
from app.arrangement.schema.html_generator import DisplayLayoutSimple
from app.arrangement.schema.persons import PersonRead
from app.arrangement.schema.rooms import RoomRead, RoomWithLocation
from app.core.mixins import CamelModelMixin
from sqlalchemy_utils import ChoiceType


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
    start: datetime.datetime
    end: datetime.datetime
    all_day: bool
    sequence_guid: Optional[str]
    serie_id: Optional[int]
    arrangement_id: Optional[int]
    event_type: Optional[Literal[EventTypeChoice.CHOICES]]
    association_type: Optional[Literal[AssociationTypeChoice.CHOICES]]

    class Config:
        orm_mode = True


class EventCreate(EventBase):
    pass


class EventRead(EventBase):
    id: int
    display_layouts: List[DisplayLayoutSimple]


class EventUpdate(CamelModelMixin):
    title: Optional[str]
    start: Optional[datetime.datetime]
    end: Optional[datetime.datetime]
    all_day: Optional[bool]
    sequence_guid: Optional[str]
    serie_id: Optional[int]
    arrangement_id: Optional[int]
    event_type: Optional[Literal[EventTypeChoice.CHOICES]]
    association_type: Optional[Literal[AssociationTypeChoice.CHOICES]]


class Config:
        orm_mode = True


class EventReadExtra(EventRead):
    arrangement: Optional[ArrangementRead]
    people: List[PersonRead]
    rooms: List[RoomRead]
    articles: List[ArticleRead]


class EventDisplayRead(CamelModelMixin):
    id: int
    title: str
    start: datetime.datetime
    end: datetime.datetime
    all_day: bool
    arrangement: ArrangementDisplayRead
    rooms: List[RoomWithLocation]
    display_layouts: List[DisplayLayoutSimple]

    class Config:
        orm_mode = True







