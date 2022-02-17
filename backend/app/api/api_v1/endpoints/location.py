from typing import List

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session
from app.core.session import get_db
from app.arrangment.models import Location, Room
from app.arrangment.schemas import LocationRead, LocationCreate, LocationUpdate, LocationReadWithRoom
from app.arrangment.schemas import RoomRead, RoomCreate, RoomReadWithLocation, RoomUpdate


location_router = loc = APIRouter()


@loc.post("/locations/", response_model=LocationRead)
def create_location(*, session: Session = Depends(get_db), location: LocationCreate):
    db_location = Location.from_orm(location)
    session.add(db_location)
    session.commit()
    session.refresh(db_location)
    return db_location


@loc.get("/locations", response_model=List[LocationRead])
def read_locations(*, session: Session = Depends(get_db), offset: int = 0, limit: int = Query(default=100, lte=100)):
    locations = session.query(Location).offset(offset).limit(limit).all()
    return locations


@loc.get("/location/{location_id}", response_model=LocationReadWithRoom)
def read_location(*, session: Session = Depends(get_db), location_id: int):
    location = session.get(Location, location_id)
    if not location:
        raise HTTPException(status_code=404, detail="location not found")
    return location


@loc.patch("/location/{location_id}", response_model=LocationRead)
def update_location(*, session: Session = Depends(get_db), location_id: int, location: LocationUpdate):
    db_location = session.get(Location, location_id)
    if not db_location:
        raise HTTPException(status_code=404, detail="location not found")
    model_data = location.dict(exclude_unset=True)
    for key, value in model_data.items():
        setattr(db_location, key, value)
    session.add(db_location)
    session.commit()
    session.refresh(db_location)
    return db_location


@loc.delete("/location/{location_id}")
def delete_location(*, session: Session = Depends(get_db), location_id: int):
    location = session.get(Location, location_id)
    if not location:
        raise HTTPException(status_code=404, detail="location not found")
    session.delete(location)
    session.commit()
    return {"ok": True}


@loc.get("/rooms", response_model=List[RoomRead])
def read_rooms(*, session: Session = Depends(get_db), offset: int = 0, limit: int = Query(default=100, lte=100)):
    rooms = session.query(Room).offset(offset).limit(limit).all()
    return rooms


@loc.get("/room/{room_id}", response_model=RoomReadWithLocation)
def read_room(*, session: Session = Depends(get_db), room_id: int):
    room = session.get(Room, room_id)
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    return room


@loc.post("/room", response_model=RoomRead)
def create_room(*, session: Session = Depends(get_db), room: RoomCreate):
    db_room = Room.from_orm(room)
    session.add(db_room)
    session.commit()
    session.refresh(db_room)
    return db_room


@loc.patch("/room/{room_id}", response_model=RoomRead)
def update_location(*, session: Session = Depends(get_db), room_id: int, room: RoomUpdate):
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
def delete_location(*, session: Session = Depends(get_db), room_id: int):
    room = session.get(Room, room_id)
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    session.delete(room)
    session.commit()
    return {"ok": True}
