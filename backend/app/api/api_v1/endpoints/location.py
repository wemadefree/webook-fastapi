from typing import List

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Field, Relationship, Session, SQLModel, create_engine, select
from app.core.session import get_db
from app.arrangment.models import Location
from app.arrangment.schemas import LocationRead, LocationCreate, LocationUpdate


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


@loc.get("/location/{location_id}", response_model=LocationRead)
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
