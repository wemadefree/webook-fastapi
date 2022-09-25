import datetime
from typing import List, Optional

from app.arrangement.schema.persons import PersonRead
from app.arrangement.schema.organizations import OrganizationRead
from app.arrangement.schema.rooms import LocationRead
from app.arrangement.schema.html_generator import DisplayLayoutSimple
from app.core.mixins import CamelModelMixin


class AudienceBase(CamelModelMixin):
    name: str
    name_en: Optional[str]
    icon_class: Optional[str]
    parent_id: Optional[int]

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
    parent_id: Optional[int]

    class Config:
        orm_mode = True


class ArrangementTypeCreate(CamelModelMixin):
    name: str
    name_en: Optional[str]
    parent_id: Optional[int]


class ArrangementBase(CamelModelMixin):
    name: str
    name_en: Optional[str]
    stages: str
    meeting_place: Optional[str]
    meeting_place_en: Optional[str]
    starts: Optional[datetime.date]
    ends: Optional[datetime.date]
    audience_id: Optional[int]
    location_id: Optional[int]
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
    location: Optional[LocationRead]
    display_layouts: List[DisplayLayoutSimple]


class ArrangementDisplayRead(CamelModelMixin):
    id: int
    name: str
    name_en: Optional[str]
    starts: Optional[datetime.date]
    ends: Optional[datetime.date]
    meeting_place: Optional[str]
    meeting_place_en: Optional[str]
    audience: Optional[AudienceRead]
    location: Optional[LocationRead]
    arrangement_type: Optional[ArrangementTypeBase]
    display_layouts: List[DisplayLayoutSimple]

    class Config:
        orm_mode = True


class ArrangementReadExtra(ArrangementRead):
    planners: List[PersonRead]
    people_participants: List[PersonRead]
    organization_participants: List[OrganizationRead]
    #notes: List[NoteRead]


class ArrangementUpdate(CamelModelMixin):
    name: Optional[str]
    stages: Optional[str]
    starts: Optional[datetime.date]
    ends: Optional[datetime.date]
    meeting_place: Optional[str]
    meeting_place_en: Optional[str]
    audience_id: Optional[int]
    location_id: Optional[int]
    responsible_id: Optional[int]
    arrangement_type_id: Optional[int]

    class Config:
        orm_mode = True



