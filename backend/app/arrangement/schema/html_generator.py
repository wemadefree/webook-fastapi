from typing import List, Optional

from app.arrangement.schema.rooms import RoomRead
from app.core.mixins import CamelModelMixin


class ScreenResourceBase(CamelModelMixin):
    screen_model: str
    items_shown: int
    room_id: Optional[int]

    class Config:
        orm_mode = True


class ScreenResourceCreate(ScreenResourceBase):
    pass


class ScreenResourceRead(ScreenResourceBase):
    id: int
    room: Optional[RoomRead]


class ScreenResourceUpdate(CamelModelMixin):
    screen_model: Optional[str]
    items_shown: Optional[int]
    room_id: Optional[int]

    class Config:
        orm_mode = True


class ScreenGroupBase(CamelModelMixin):
    group_name: str
    group_name_en: Optional[str]
    quantity: int

    class Config:
        orm_mode = True


class ScreenGroupRead(ScreenGroupBase):
    id: int

    screens: List[ScreenResourceRead]


class ScreenGroupCreate(ScreenGroupBase):
    pass


class ScreenGroupUpdate(CamelModelMixin):
    group_name: Optional[str]
    quantity: Optional[int]

    class Config:
        orm_mode = True


class DisplayLayoutSettingBase(CamelModelMixin):
    name: str
    html_template: str
    css_template: str
    file_output_path: str

    class Config:
        orm_mode = True


class DisplayLayoutSettingRead(DisplayLayoutSettingBase):
    id: int


class DisplayLayoutSettingCreate(DisplayLayoutSettingBase):
    pass


class DisplayLayoutSettingUpdate(CamelModelMixin):
    name: Optional[str]
    html_template: Optional[str]
    css_template: Optional[str]
    file_output_path: Optional[str]

    class Config:
        orm_mode = True


class DisplayLayoutBase(CamelModelMixin):
    name: str
    description: str
    items_shown: int
    is_room_based: bool
    all_events: bool
    is_active: bool
    setting_id: Optional[int]

    class Config:
        orm_mode = True


class DisplayLayoutRead(DisplayLayoutBase):
    id: int

    setting: Optional[DisplayLayoutSettingRead]
    screens: List[ScreenResourceRead]
    groups: List[ScreenGroupRead]


class DisplayLayoutSimple(CamelModelMixin):
    name: str

    class Config:
        orm_mode = True


class DisplayLayoutCreate(DisplayLayoutBase):
    pass


class DisplayLayoutUpdate(CamelModelMixin):
    name: Optional[str]
    description: Optional[str]
    items_shown: Optional[int]
    is_room_based: Optional[bool]
    is_active: Optional[bool]
    all_events: Optional[bool]
    setting_id: Optional[int]

    class Config:
        orm_mode = True












