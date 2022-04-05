from typing import List

from fastapi import APIRouter, Depends, Query
from sqlmodel import Session
from app.core.session import get_sqlmodel_sesion as get_session
from app.arrangement.model.basemodels import Room, Location, ScreenResource, ScreenGroup, \
    DisplayLayout, DisplayLayoutSetting
from app.arrangement.schema.html_generator import DisplayLayoutSettingRead, DisplayLayoutSettingCreate, \
    DisplayLayoutSettingUpdate, DisplayLayoutRead, DisplayLayoutCreate, DisplayLayoutUpdate, \
    ScreenResourceRead, ScreenResourceCreate, ScreenResourceUpdate, ScreenGroupRead, \
    ScreenGroupCreate, ScreenGroupUpdate
from app.arrangement.factory import CrudManager

html_router = html = APIRouter()


@html.post("/screenresource", response_model=ScreenResourceRead)
def create_screen_resource(*, session: Session = Depends(get_session), screen: ScreenResourceCreate):
    item = CrudManager(ScreenResource).create_item(session, screen)
    return item


@html.get("/screenresources", response_model=List[ScreenResourceRead])
def list_screen_resources(*, session: Session = Depends(get_session), offset: int = 0,
                          limit: int = Query(default=100, lte=100)):
    items = CrudManager(ScreenResource).read_items(session, offset, limit)
    return items


@html.get("/screenresource/{screen_id}", response_model=ScreenResourceRead)
def read_screen_resource(*, session: Session = Depends(get_session), screen_id: int):
    item = CrudManager(ScreenResource).read_item(session, screen_id)
    return item


@html.patch("/screenresource/{screen_id}", response_model=ScreenResourceRead)
def update_screen_resource(*, session: Session = Depends(get_session), screen_id: int, screen: ScreenResourceUpdate):
    item = CrudManager(ScreenResource).edit_item(session, screen_id, screen)
    return item


@html.delete("/screenresource/{screen_id}")
def delete_screen_resource(*, session: Session = Depends(get_session), screen_id: int):
    return CrudManager(ScreenResource).delete_item(session, screen_id)


@html.post("/screengroup", response_model=ScreenGroupRead)
def create_screen_group(*, session: Session = Depends(get_session), screen: ScreenGroupCreate):
    item = CrudManager(ScreenGroup).create_item(session, screen)
    return item


@html.get("/screengroups", response_model=List[ScreenGroupRead])
def list_screen_groups(*, session: Session = Depends(get_session), offset: int = 0,
                       limit: int = Query(default=100, lte=100)):
    items = CrudManager(ScreenGroup).read_items(session, offset, limit)
    return items


@html.get("/screengroup/{group_id}", response_model=ScreenGroupRead)
def read_screen_group(*, session: Session = Depends(get_session), group_id: int):
    item = CrudManager(ScreenGroup).read_item(session, group_id)
    return item


@html.patch("/screengroup/{group_id}", response_model=ScreenGroupRead)
def update_screen_group(*, session: Session = Depends(get_session), group_id: int, group: ScreenGroupUpdate):
    item = CrudManager(ScreenGroup).edit_item(session, group_id, group)
    return item


@html.delete("/screengroup/{group_id}")
def delete_screen_group(*, session: Session = Depends(get_session), group_id: int):
    return CrudManager(ScreenGroup).delete_item(session, group_id)


@html.post("/screengroup/{group_id}/screenresource/{screen_id}", response_model=ScreenGroupRead)
def add_screenresource_to_group(*, session: Session = Depends(get_session), group_id: int, screen_id: int):
    db_grp = CrudManager(ScreenGroup).read_item(session, group_id)
    if db_grp:
        db_screen = CrudManager(ScreenResource).read_item(session, screen_id)
        if db_screen:
            db_grp.screens.append(db_screen)
        db_grp = CrudManager(ScreenGroup).edit_item(session, group_id, db_grp)
    return db_grp


@html.delete("/screengroup/{group_id}/screenresource/{screen_id}", response_model=ScreenGroupRead)
def remove_screenresource_from_group(*, session: Session = Depends(get_session), group_id: int, screen_id: int):
    db_grp = CrudManager(ScreenGroup).read_item(session, group_id)
    if db_grp:
        for per in db_grp.screens:
            if per.id == screen_id:
                db_grp.screens.remove(per)
                break
        db_grp = CrudManager(ScreenGroup).edit_item(session, group_id, db_grp)
    return db_grp


@html.post("/displaylayout", response_model=DisplayLayoutRead)
def create_display_layout(*, session: Session = Depends(get_session), screen: DisplayLayoutCreate):
    item = CrudManager(DisplayLayout).create_item(session, screen)
    return item


@html.get("/displaylayouts", response_model=List[DisplayLayoutRead])
def list_display_layouts(*, session: Session = Depends(get_session), offset: int = 0,
                         limit: int = Query(default=100, lte=100)):
    items = CrudManager(DisplayLayout).read_items(session, offset, limit)
    return items


@html.get("/displaylayout/{layout_id}", response_model=DisplayLayoutRead)
def read_display_layout(*, session: Session = Depends(get_session), layout_id: int):
    item = CrudManager(DisplayLayout).read_item(session, layout_id)
    return item


@html.patch("/displaylayout/{layout_id}", response_model=DisplayLayoutRead)
def update_display_layout(*, session: Session = Depends(get_session), layout_id: int, layout: DisplayLayoutUpdate):
    item = CrudManager(DisplayLayout).edit_item(session, layout_id, layout)
    return item


@html.delete("/displaylayout/{layout_id}")
def delete_display_layout(*, session: Session = Depends(get_session), layout_id: int):
    return CrudManager(DisplayLayout).delete_item(session, layout_id)


@html.post("/displaylayout/{layout_id}/screenresource/{screen_id}", response_model=DisplayLayoutRead)
def add_screenresource_to_display_layout(*, session: Session = Depends(get_session), layout_id: int, screen_id: int):
    db_lay = CrudManager(DisplayLayout).read_item(session, layout_id)
    if db_lay:
        db_screen = CrudManager(ScreenResource).read_item(session, screen_id)
        if db_screen:
            db_lay.screens.append(db_screen)
        db_lay = CrudManager(DisplayLayout).edit_item(session, layout_id, db_lay)
    return db_lay


@html.delete("/displaylayout/{layout_id}/screenresource/{screen_id}", response_model=DisplayLayoutRead)
def remove_screenresource_from_display_layout(*, session: Session = Depends(get_session),
                                              screen_id: int, layout_id: int):
    db_lay = CrudManager(DisplayLayout).read_item(session, layout_id)
    if db_lay:
        for per in db_lay.screens:
            if per.id == screen_id:
                db_lay.screens.remove(per)
                break
        db_lay = CrudManager(DisplayLayout).edit_item(session, layout_id, db_lay)
    return db_lay


@html.post("/displaylayout/{layout_id}/screengroup/{group_id}", response_model=DisplayLayoutRead)
def add_screen_group_to_display_layout(*, session: Session = Depends(get_session), layout_id: int, group_id: int):
    db_lay = CrudManager(DisplayLayout).read_item(session, layout_id)
    if db_lay:
        db_group = CrudManager(ScreenGroup).read_item(session, group_id)
        if db_group:
            db_lay.groups.append(db_group)
        db_cal = CrudManager(DisplayLayout).edit_item(session, layout_id, db_lay)
    return db_cal


@html.delete("/displaylayout/{layout_id}/screengroup/{group_id}", response_model=DisplayLayoutRead)
def remove_screengroup_from_display_layout(*, session: Session = Depends(get_session), group_id: int,
                                           layout_id: int):
    db_lay = CrudManager(DisplayLayout).read_item(session, layout_id)
    if db_lay:
        for per in db_lay.groups:
            if per.id == group_id:
                db_lay.groups.remove(per)
                break
        db_lay = CrudManager(DisplayLayout).edit_item(session, layout_id, db_lay)
    return db_lay


@html.post("/layoutsetting", response_model=DisplayLayoutSettingRead)
def create_layout_setting(*, session: Session = Depends(get_session), setting: DisplayLayoutSettingCreate):
    item = CrudManager(DisplayLayoutSetting).create_item(session, setting)
    return item


@html.get("/layoutsettings", response_model=List[DisplayLayoutSettingRead])
def read_layout_settings(*, session: Session = Depends(get_session), offset: int = 0,
                         limit: int = Query(default=100, lte=100)):
    items = CrudManager(DisplayLayoutSetting).read_items(session, offset, limit)
    return items


@html.get("/layoutsetting/{setting_id}", response_model=DisplayLayoutSettingRead)
def read_layout_setting(*, session: Session = Depends(get_session), setting_id: int):
    item = CrudManager(DisplayLayoutSetting).read_item(session, setting_id)
    return item


@html.patch("/layoutsetting/{setting_id}", response_model=DisplayLayoutSettingRead)
def update_layout_setting(*, session: Session = Depends(get_session), setting_id: int,
                          setting: DisplayLayoutSettingUpdate):
    item = CrudManager(DisplayLayoutSetting).edit_item(session, setting_id, setting)
    return item


@html.delete("/layoutsetting/{setting_id}")
def delete_layout_setting(*, session: Session = Depends(get_session), setting_id: int):
    return CrudManager(DisplayLayoutSetting).delete_item(session, setting_id)


