import datetime
from typing import List, Optional
from sqlmodel import SQLModel

from app.arrangement.model.basemodels import StageChoices
from app.arrangement.schema.persons import PersonRead, NoteRead, NoteUpdate
from app.arrangement.schema.organizations import OrganizationRead
from app.arrangement.schema.html_generator import DisplayLayoutSimple
from app.core.mixins import CamelCaseMixin


class AudienceBase(SQLModel, CamelCaseMixin):
    name: str
    name_en: str
    icon_class: str


class AudienceRead(AudienceBase):
    id: int


class AudienceCreate(AudienceBase):
    pass


class AudienceUpdate(SQLModel, CamelCaseMixin):
    name: Optional[str]
    icon_class: Optional[str]


class TimeLineEventBase(SQLModel, CamelCaseMixin):
    content: str
    stamp: datetime.datetime


class TimeLineEventCreate(TimeLineEventBase):
    pass


class TimeLineEventRead(TimeLineEventBase):
    id: int


class TimeLineEventUpdate(SQLModel, CamelCaseMixin):
    content: Optional[str]
    stamp: Optional[datetime.datetime]


class TimeLineEventAddOrUpdate(SQLModel, CamelCaseMixin):
    id: int
    content: Optional[str]
    stamp: Optional[datetime.datetime]


class ArrangementTypeBase(SQLModel, CamelCaseMixin):
    id: Optional[int]
    name: str
    name_en: Optional[str]


class ArrangementTypeCreate(SQLModel, CamelCaseMixin):
    name: str
    name_en: Optional[str]


class ArrangementBase(SQLModel, CamelCaseMixin):
    name: str
    name_en: str
    stages: StageChoices
    starts: datetime.date
    ends: datetime.date
    audience_id: Optional[int]
    responsible_id: Optional[int]
    arrangement_type_id: Optional[int]


class ArrangementCreate(ArrangementBase):
    pass


class ArrangementRead(ArrangementBase):
    id: int
    audience: Optional[AudienceRead]
    arrangement_type: Optional[ArrangementTypeBase]
    responsible: Optional[PersonRead]
    display_layouts: List[DisplayLayoutSimple]


class ArrangementHTMLGenerator(SQLModel, CamelCaseMixin):
    id: int
    name: str
    starts: datetime.date
    ends: datetime.date
    audience: Optional[AudienceRead]
    arrangement_type: Optional[ArrangementTypeBase]


class ArrangementReadExtra(ArrangementRead):
    timeline_events: List[TimeLineEventRead]
    planners: List[PersonRead]
    people_participants: List[PersonRead]
    organization_participants: List[OrganizationRead]
    notes: List[NoteRead]


class ArrangementUpdate(SQLModel, CamelCaseMixin):
    name: Optional[str]
    stages: Optional[StageChoices]
    starts: Optional[datetime.date]
    ends: Optional[datetime.date]
    audience_id: Optional[int]
    responsible_id: Optional[int]
    arrangement_type_id: Optional[int]



