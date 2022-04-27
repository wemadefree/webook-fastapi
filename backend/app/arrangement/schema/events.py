import datetime
from typing import List, Optional
from sqlmodel import SQLModel

from app.arrangement.schema.arrangements import ArrangementRead, ArrangementDisplayRead
from app.arrangement.schema.html_generator import DisplayLayoutSimple
from app.arrangement.schema.persons import PersonRead, NoteRead, ConfirmationRecieptRead
from app.arrangement.schema.services import LooseServiceRequisitionRead, ServiceProviderRead
from app.arrangement.schema.rooms import RoomRead, RoomWithLocation
from app.core.mixins import CamelCaseMixin


class ArticleBase(SQLModel, CamelCaseMixin):
    name: str


class ArticleRead(ArticleBase):
    id: int


class ArticleCreate(ArticleBase):
    pass


class ArticleUpdate(SQLModel, CamelCaseMixin):
    name: Optional[str]


class ArticleAddOrUpdate(ArticleUpdate):
    id: int


class EventSerieBase(SQLModel, CamelCaseMixin):
    arrangement_id: Optional[int]


class EventSerieCreate(EventSerieBase):
    pass


class EventSerieRead(EventSerieBase):
    id: int


class EventSerieUpdate(SQLModel):
    arrangement_id: Optional[int]


class EventSerieReadExtra(EventSerieRead):
    arrangement: Optional[ArrangementRead]


class EventBase(SQLModel, CamelCaseMixin):
    title: str
    start: datetime.datetime
    end: datetime.datetime
    all_day: bool
    sequence_guid: str
    color: str
    serie_id: Optional[int]
    arrangement_id: Optional[int]


class EventCreate(EventBase):
    pass


class EventRead(EventBase):
    id: int
    display_layouts: List[DisplayLayoutSimple]


class EventUpdate(SQLModel, CamelCaseMixin):
    title: Optional[str]
    start: Optional[datetime.datetime]
    end: Optional[datetime.datetime]
    all_day: Optional[bool]
    sequence_guid: Optional[str]
    color: Optional[str]
    serie_id: Optional[int]
    arrangement_id: Optional[int]


class EventReadExtra(EventRead):
    arrangement: Optional[ArrangementRead]
    serie: Optional[EventSerieRead]
    people: List[PersonRead]
    rooms: List[RoomRead]
    loose_requisitions: List[LooseServiceRequisitionRead]
    articles: List[ArticleRead]
    #notes: List[NoteRead]


class EventDisplayRead(SQLModel, CamelCaseMixin):
    id: int
    title: str
    start: datetime.datetime
    end: datetime.datetime
    all_day: bool
    arrangement: ArrangementDisplayRead
    rooms: List[RoomWithLocation]
    display_layouts: List[DisplayLayoutSimple]


class EventServiceBase(SQLModel, CamelCaseMixin):
    receipt_id: Optional[int]
    event_id: Optional[int]
    service_provider_id: Optional[int]


class EventServiceRead(EventServiceBase):
    id: int


class EventServiceCreate(EventServiceBase):
    pass


class EventServiceUpdate(SQLModel, CamelCaseMixin):
    receipt_id: Optional[int]
    event_id: Optional[int]
    service_provider_id: Optional[int]


class EventServiceReadExtra(EventServiceRead):
    receipt:  Optional[ConfirmationRecieptRead]
    event:  Optional[EventRead]
    service_provider: Optional[ServiceProviderRead]
    notes: Optional[List[NoteRead]]
    associated_people: Optional[List[PersonRead]]


