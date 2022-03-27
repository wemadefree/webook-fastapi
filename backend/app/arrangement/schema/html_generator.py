from typing import List, Optional
from sqlmodel import SQLModel, Field

from app.core.mixins import CamelCaseMixin
from app.arrangement.schema.rooms import LocationRead


class ScreenResourceBase(SQLModel, CamelCaseMixin):
    name: str
    description: str
    quantity: int
    room_screen: bool
    location_id: Optional[int]


class ScreenResourceCreate(ScreenResourceBase):
    pass


class ScreenResourceRead(ScreenResourceBase):
    id: int
    location: Optional[LocationRead]


class ScreenResourceUpdate(SQLModel, CamelCaseMixin):
    name: Optional[str]
    description: Optional[str]
    quantity: Optional[int]
    room_screen: Optional[bool]
    location_id: Optional[int]


class ScreenGroupBase(SQLModel, CamelCaseMixin):
    group_name: str
    description: str
    quantity: int


class ScreenGroupRead(ScreenGroupBase):
    id: int

    screens: List[ScreenResourceRead]


class ScreenGroupCreate(ScreenGroupBase):
    pass


class ScreenGroupUpdate(SQLModel, CamelCaseMixin):
    group_name: Optional[str]
    description: Optional[str]
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
    room_based: bool
    active: bool
    setting_id: Optional[int]


class DisplayLayoutRead(DisplayLayoutBase):
    id: int

    setting: Optional[DisplayLayoutSettingRead]
    screens: List[ScreenResourceRead]
    groups: List[ScreenGroupRead]


class DisplayLayoutCreate(DisplayLayoutBase):
    pass


class DisplayLayoutUpdate(SQLModel, CamelCaseMixin):
    name: Optional[str]
    description: Optional[str]
    room_based: Optional[bool]
    active: Optional[bool]
    setting_id: Optional[int]












