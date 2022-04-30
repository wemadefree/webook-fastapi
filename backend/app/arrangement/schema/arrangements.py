import datetime
from typing import List, Optional
from pydantic import BaseModel

from app.arrangement.model.basemodels import StageChoices
from app.arrangement.schema.persons import PersonRead
from app.arrangement.schema.organizations import OrganizationRead
from app.arrangement.schema.html_generator import DisplayLayoutSimple
from app.core.mixins import CamelModelMixin
from app.core.session import Base
from app.core.utils import to_camel


class AudienceBase(CamelModelMixin):
    name: str
    name_en: Optional[str]
    icon_class: Optional[str]

    class Config:
        orm_mode = True


class AudienceRead(AudienceBase):
    id: int


class AudienceCreate(AudienceBase):
    pass


class AudienceUpdate(CamelModelMixin):
    name: Optional[str]
    name_en: Optional[str]
    icon_class: Optional[str]


class TimeLineEventBase(CamelModelMixin):
    content: str
    stamp: datetime.datetime

    class Config:
        orm_mode = True


class TimeLineEventCreate(TimeLineEventBase):
    pass


class TimeLineEventRead(TimeLineEventBase):
    id: int


class TimeLineEventUpdate(CamelModelMixin):
    content: Optional[str]
    stamp: Optional[datetime.datetime]


class TimeLineEventAddOrUpdate(CamelModelMixin):
    id: int
    content: Optional[str]
    stamp: Optional[datetime.datetime]


class ArrangementTypeBase(CamelModelMixin):
    id: Optional[int]
    name: str
    name_en: Optional[str]

    class Config:
        orm_mode = True


class ArrangementTypeCreate(CamelModelMixin):
    name: str
    name_en: Optional[str]


class ArrangementBase(CamelModelMixin):
    name: str
    name_en: Optional[str]
    stages: str
    starts: Optional[datetime.date]
    ends: Optional[datetime.date]
    audience_id: Optional[int]
    responsible_id: Optional[int]
    arrangement_type_id: Optional[int]

    class Config:
        orm_mode = True


class ArrangementCreate(ArrangementBase):
    pass


class ArrangementRead(ArrangementBase):
    id: int
    audience: Optional[AudienceRead]
    arrangement_type: Optional[ArrangementTypeBase]
    responsible: Optional[PersonRead]
    display_layouts: List[DisplayLayoutSimple]


class ArrangementDisplayRead(CamelModelMixin):
    id: int
    name: str
    name_en: Optional[str]
    starts: Optional[datetime.date]
    ends: Optional[datetime.date]
    audience: Optional[AudienceRead]
    arrangement_type: Optional[ArrangementTypeBase]
    display_layouts: List[DisplayLayoutSimple]

    class Config:
        orm_mode = True


class ArrangementReadExtra(ArrangementRead):
    timeline_events: List[TimeLineEventRead]
    planners: List[PersonRead]
    people_participants: List[PersonRead]
    organization_participants: List[OrganizationRead]
    #notes: List[NoteRead]


class ArrangementUpdate(CamelModelMixin):
    name: Optional[str]
    stages: Optional[str]
    starts: Optional[datetime.date]
    ends: Optional[datetime.date]
    audience_id: Optional[int]
    responsible_id: Optional[int]
    arrangement_type_id: Optional[int]

    class Config:
        orm_mode = True



