from typing import List, Optional
from sqlmodel import SQLModel, Field

from app.core.mixins import CamelCaseMixin
from app.arrangement.schema.rooms import LocationRead


class ScreenResourceBase(SQLModel, CamelCaseMixin):
    name: str
    name_en: Optional[str]
    quantity: int
    is_room_screen: bool
    location_id: Optional[int]


class ScreenResourceCreate(ScreenResourceBase):
    pass


class ScreenResourceRead(ScreenResourceBase):
    id: int
    location: Optional[LocationRead]


class ScreenResourceUpdate(SQLModel, CamelCaseMixin):
    name: Optional[str]
    name_en: Optional[str]
    quantity: Optional[int]
    is_room_screen: Optional[bool]
    location_id: Optional[int]


class ScreenGroupBase(SQLModel, CamelCaseMixin):
    group_name: str
    group_name_en: Optional[str]
    quantity: int


class ScreenGroupRead(ScreenGroupBase):
    id: int

    screens: List[ScreenResourceRead]


class ScreenGroupCreate(ScreenGroupBase):
    pass


class ScreenGroupUpdate(SQLModel, CamelCaseMixin):
    group_name: Optional[str]
    quantity: Optional[int]


class DisplayLayoutSettingBase(SQLModel, CamelCaseMixin):
    name: str
    html_template: str
    css_template: str
    file_output_path: str


class DisplayLayoutSettingRead(DisplayLayoutSettingBase):
    id: int


class DisplayLayoutSettingCreate(DisplayLayoutSettingBase):
    pass


class DisplayLayoutSettingUpdate(SQLModel, CamelCaseMixin):
    name: Optional[str]
    html_template: Optional[str]
    css_template: Optional[str]
    file_output_path: Optional[str]


class DisplayLayoutBase(SQLModel, CamelCaseMixin):
    name: str
    description: str
    is_room_based: bool
    all_events: bool
    is_active: bool
    setting_id: Optional[int]


class DisplayLayoutRead(DisplayLayoutBase):
    id: int

    setting: Optional[DisplayLayoutSettingRead]
    screens: List[ScreenResourceRead]
    groups: List[ScreenGroupRead]


class DisplayLayoutSimple(SQLModel, CamelCaseMixin):
    name: str


class DisplayLayoutCreate(DisplayLayoutBase):
    pass


class DisplayLayoutUpdate(SQLModel, CamelCaseMixin):
    name: Optional[str]
    description: Optional[str]
    is_room_based: Optional[bool]
    is_active: Optional[bool]
    all_events: Optional[bool]
    setting_id: Optional[int]












