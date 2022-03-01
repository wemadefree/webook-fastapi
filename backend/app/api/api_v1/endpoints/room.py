from typing import List

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session
from app.core.session import get_sqlmodel_sesion as get_session
from app.arrangement.model.basemodels import Location, Room
from app.arrangement.schema.rooms import LocationRead, LocationCreate, LocationUpdate, LocationReadWithRoom
from app.arrangement.schema.rooms import RoomRead, RoomCreate, RoomReadWithLocation, RoomUpdate
from app.arrangement.factory import CrudManager

location_router = loc = APIRouter()


@loc.post("/locations/", response_model=LocationRead)
def create_location(*, session: Session = Depends(get_session), location: LocationCreate):
    location_item = CrudManager(Location).read_item(session, location)
    return location_item


@loc.get("/locations", response_model=List[LocationRead])
def read_locations(*, session: Session = Depends(get_session), offset: int = 0, limit: int = Query(default=100, lte=100)):
    locations = CrudManager(LocationRead).read_items(session, offset, limit)
    return locations


@loc.get("/location/{location_id}", response_model=LocationReadWithRoom)
def read_location(*, session: Session = Depends(get_session), location_id: int):
    location = CrudManager(Location).read_item(session, location_id)
    return location


@loc.patch("/location/{location_id}", response_model=LocationRead)
def update_location(*, session: Session = Depends(get_session), location_id: int, location: LocationUpdate):
    location_item = CrudManager(Location).edit_item(session, location_id, location)
    return location_item


@loc.delete("/location/{location_id}")
def delete_location(*, session: Session = Depends(get_session), location_id: int):
    location = CrudManager(Location).delete_item(session, location_id)
    return location


@loc.get("/rooms", response_model=List[RoomRead])
def read_rooms(*, session: Session = Depends(get_session), offset: int = 0, limit: int = Query(default=100, lte=100)):
    rooms = session.query(Room).offset(offset).limit(limit).all()
    return rooms


@loc.get("/room/{room_id}", response_model=RoomReadWithLocation)
def read_room(*, session: Session = Depends(get_session), room_id: int):
    room = session.get(Room, room_id)
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    return room


@loc.post("/room", response_model=RoomRead)
def create_room(*, session: Session = Depends(get_session), room: RoomCreate):
    db_room = Room.from_orm(room)
    session.add(db_room)
    session.commit()
    session.refresh(db_room)
    return db_room


@loc.patch("/room/{room_id}", response_model=RoomRead)
def update_room(*, session: Session = Depends(get_session), room_id: int, room: RoomUpdate):
    db_room = session.get(Room, room_id)
    if not db_room:
        raise HTTPException(status_code=404, detail="Room not found")
    model_data = room.dict(exclude_unset=True)
    for key, value in model_data.items():
        setattr(db_room, key, value)
    session.add(db_room)
    session.commit()
    session.refresh(db_room)
    return db_room


@loc.delete("/room/{room_id}")
def delete_location(*, session: Session = Depends(get_session), room_id: int):
    room = session.get(Room, room_id)
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    session.delete(room)
    session.commit()
    return {"ok": True}
