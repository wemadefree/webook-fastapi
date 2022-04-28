from datetime import datetime
from datetime import timedelta
from typing import List

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select
from app.core.session import get_sqlmodel_sesion as get_session
from app.arrangement.model.basemodels import Article, DisplayLayout, EventSerie, Event, Arrangement, EventService, LooseServiceRequisition, Note, Person, Room
from app.arrangement.schema.events import EventSerieRead, EventSerieReadExtra, EventSerieCreate, EventSerieUpdate
from app.arrangement.schema.events import EventRead, EventReadExtra, EventDisplayRead, EventCreate, EventUpdate
from app.arrangement.schema.events import EventServiceRead, EventServiceReadExtra, EventServiceCreate, EventServiceUpdate
from app.arrangement.schema.events import ArticleRead, ArticleAddOrUpdate, ArticleCreate, ArticleUpdate

from app.arrangement.factory import CrudManager

event_router = evt = APIRouter()
article_router = art = APIRouter()
event_service_router = srv = APIRouter()


@art.post("/articles", response_model=ArticleRead)
def create_articles(*, session: Session = Depends(get_session), article: ArticleCreate):
    article_item = CrudManager(Article).create_item(session, article)
    return article_item


@art.get("/articles", response_model=List[ArticleRead])
def read_articles(*, session: Session = Depends(get_session), offset: int = 0, limit: int = Query(default=100, lte=100)):
    articles = CrudManager(Article).read_items(session, offset, limit)
    return articles


@art.get("/article/{article_id}", response_model=ArticleRead)
def read_article(*, session: Session = Depends(get_session), article_id: int):
    article_item = CrudManager(Article).read_item(session, article_id)
    return article_item


@art.patch("/article/{article_id}", response_model=ArticleRead)
def update_article(*, session: Session = Depends(get_session), article_id: int, article: ArticleUpdate):
    article_item = CrudManager(Article).edit_item(session, article_id, article)
    return article_item


@art.delete("/article/{article_id}")
def delete_article(*, session: Session = Depends(get_session), article_id: int):
    return CrudManager(Article).delete_item(session, article_id)


@evt.post("/events", response_model=EventReadExtra)
def create_event(*, session: Session = Depends(get_session), event: EventCreate):
    event_item = CrudManager(Event).create_item(session, event)
    return event_item


@evt.get("/events", response_model=List[EventRead])
def read_event(*, session: Session = Depends(get_session), offset: int = 0, limit: int = Query(default=100, lte=100)):
    events = CrudManager(Event).read_items(session, offset, limit)
    return events


@evt.get("/events/current", response_model=List[EventRead])
def get_current_events(*, session: Session = Depends(get_session)):
    now = datetime.now()
    events = session.query(Event).where(now > Event.start).where(now < Event.end).order_by(Event.start).all()
    return events


@evt.get("/events/next_on_schedule", response_model=List[EventDisplayRead])
def get_events_next_on_schedule(*, session: Session = Depends(get_session), days_ahead: int = Query(default=5), limit: int = Query(default=30, lte=30)):
    '''Add filter by location'''
    now = datetime.now()
    end_datetime = now + timedelta(days=days_ahead)
    events = session.query(Event).where(Event.start >= now).where(Event.start < end_datetime).order_by(Event.start).limit(limit).all()
    return events

"""
@evt.get("/events/starting_next", response_model=List[EventDisplayRead])
def get_events_starting_next(*, session: Session = Depends(get_session)):
    '''Add filter by location'''
    statement = select(Event.title, Arrangement.name).where(Event.arrangement_id == Arrangement.id).where(Arrangement.show_in_mmg == True)
    results = session.exec(statement)
    for event, arrangement in results:
        print("Event:", event, "Arrangement:", arrangement)
    now = datetime.now()
    today_max_time = datetime.combine(datetime.today(), datetime.max.time())
    events = session.query(Event).where(Event.start >= now).where(Event.start <= today_max_time).order_by(Event.start).all()
    return events
"""

@evt.get("/event/{event_id}", response_model=EventReadExtra)
def read_event(*, session: Session = Depends(get_session), event_id: int):
    event_item = CrudManager(Event).read_item(session, event_id)
    return event_item


@evt.patch("/event/{event_id}", response_model=EventReadExtra)
def update_event(*, session: Session = Depends(get_session), event_id: int, event: EventUpdate):
    event_item = CrudManager(Event).edit_item(session, event_id, event)
    return event_item


@evt.delete("/event/{event_id}")
def delete_event(*, session: Session = Depends(get_session), event_id: int):
    return CrudManager(Event).delete_item(session, event_id)


@evt.post("/event/{event_id}/display_layout/{layout_id}", response_model=EventReadExtra)
def add_event_display_configuration(*, session: Session = Depends(get_session), event_id: int, layout_id: int):
    db_event = CrudManager(Event).read_item(session, event_id)
    if db_event:
        db_conf = CrudManager(DisplayLayout).read_item(session, layout_id)
        if db_conf:
            db_event.display_layouts.append(db_conf)
        db_event = CrudManager(Event).edit_item(session, event_id, db_event)
    return db_event


@evt.delete("/event/{event_id}/display_layout/{layout_id}", response_model=EventReadExtra)
def remove_event_display_configuration(*, session: Session = Depends(get_session), event_id: int, layout_id: int):
    db_event = CrudManager(Event).read_item(session, event_id)
    if db_event:
        for per in db_event.display_layouts:
            if per.id == layout_id:
                db_event.display_layouts.remove(per)
                break
        db_event = CrudManager(Event).edit_item(session, event_id, db_event)
    return db_event


@evt.post("/event/{event_id}/room/{room_id}", response_model=EventReadExtra)
def add_room_to_event(*, session: Session = Depends(get_session), event_id: int, room_id: int):
    db_cal = CrudManager(Event).read_item(session, event_id)
    if db_cal:
        db_room = CrudManager(Room).read_item(session, room_id)
        if db_room:
            db_cal.rooms.append(db_room)
        db_cal = CrudManager(Event).edit_item(session, event_id, db_cal)
    return db_cal


@evt.delete("/event/{event_id}/room/{room_id}", response_model=EventReadExtra)
def remove_room_from_event(*, session: Session = Depends(get_session), event_id: int, room_id: int):
    db_cal = CrudManager(Event).read_item(session, event_id)
    if db_cal:
        for per in db_cal.rooms:
            if per.id == room_id:
                db_cal.rooms.remove(per)
                break
        db_cal = CrudManager(Event).edit_item(session, event_id, db_cal)
    return db_cal


@evt.post("/event/{event_id}/article/{article_id}", response_model=EventReadExtra)
def add_article_to_event(*, session: Session = Depends(get_session), event_id: int, article_id: int):
    db_evt = CrudManager(Event).read_item(session, event_id)
    if db_evt:
        db_art = CrudManager(Article).read_item(session, article_id)
        if db_art:
            db_evt.articles.append(db_art)
        db_evt = CrudManager(Event).edit_item(session, event_id, db_evt)
    return db_evt


@evt.delete("/event/{event_id}/article/{article_id}", response_model=EventReadExtra)
def remove_articles_from_event(*, session: Session = Depends(get_session), event_id: int, article_id: int):
    db_cal = CrudManager(Event).read_item(session, event_id)
    if db_cal:
        for per in db_cal.articles:
            if per.id == article_id:
                db_cal.articles.remove(per)
                break
        db_cal = CrudManager(Event).edit_item(session, event_id, db_cal)
    return db_cal

"""
@evt.post("/event/{event_id}/requisition/{requisition_id}", response_model=EventReadExtra)
def add_requisition_to_event(*, session: Session = Depends(get_session), event_id: int, requisition_id: int):
    db_evt = CrudManager(Event).read_item(session, event_id)
    if db_evt:
        db_requisition = CrudManager(LooseServiceRequisition).read_item(session, requisition_id)
        if db_requisition:
            db_evt.loose_requisitions.append(db_requisition)
        db_evt = CrudManager(Event).edit_item(session, event_id, db_evt)
    return db_evt


@evt.delete("/event/{event_id}/requisition/{requisition_id}", response_model=EventReadExtra)
def remove_requisition_to_event(*, session: Session = Depends(get_session), event_id: int, requisition_id: int):
    db_evt = CrudManager(Event).read_item(session, event_id)
    if db_evt:
        for per in db_evt.loose_requisitions:
            if per.id == requisition_id:
                db_evt.loose_requisitions.remove(per)
                break
        db_cal = CrudManager(Event).edit_item(session, event_id, db_evt)
    return db_cal
"""

@evt.post("/event/{event_id}/person/{person_id}", response_model=EventReadExtra)
def add_people_to_event(*, session: Session = Depends(get_session), org_id: int, person_id: int):
    db_event = CrudManager(Event).read_item(session, org_id)
    if db_event:
        db_person = CrudManager(Person).read_item(session, person_id)
        if db_person:
            db_event.people.append(db_person)
        db_event = CrudManager(Event).edit_item(session, org_id, db_event)
    return db_event


@evt.delete("/event/{event_id}/person/{person_id}", response_model=EventReadExtra)
def remove_people_from_event(*, session: Session = Depends(get_session), org_id: int, person_id: int):
    db_event = CrudManager(Event).read_item(session, org_id)
    if db_event:
        for per in db_event.people:
            if per.id == person_id:
                db_event.people.remove(per)
                break
        db_event = CrudManager(Event).edit_item(session, person_id, db_event)
    return db_event

"""
@evt.post("/event/{event_id}/note/{note_id}", response_model=EventReadExtra)
def add_note_to_event(*, session: Session = Depends(get_session), event_id: int, note_id: int):
    db_event = CrudManager(Event).read_item(session, event_id)
    if db_event:
        db_note = CrudManager(Note).read_item(session, note_id)
        if db_event:
            db_event.notes.append(db_note)
        db_event = CrudManager(Event).edit_item(session, event_id, db_event)
    return db_event


@evt.delete("/event/{event_id}/note/{note_id}", response_model=EventReadExtra)
def delete_note_from_event(*, session: Session = Depends(get_session), event_id: int, note_id: int):
    db_event = CrudManager(Event).read_item(session, event_id)
    if db_event:
        for per in db_event.notes:
            if per.id == note_id:
                db_event.notes.remove(per)
                break
        db_event = CrudManager(Event).edit_item(session, note_id, db_event)
    return db_event
"""

@evt.post("/eventseries", response_model=EventSerieReadExtra)
def create_eventserie(*, session: Session = Depends(get_session), eventserie: EventSerieCreate):
    eventserie_item = CrudManager(EventSerie).create_item(session, eventserie)
    return eventserie_item


@evt.get("/eventseries", response_model=List[EventSerieRead])
def read_eventseries(*, session: Session = Depends(get_session), offset: int = 0, limit: int = Query(default=100, lte=100)):
    eventseries = CrudManager(EventSerie).read_items(session, offset, limit)
    return eventseries


@evt.get("/eventserie/{eventserie_id}", response_model=EventSerieReadExtra)
def read_eventserie(*, session: Session = Depends(get_session), eventserie_id: int):
    eventserie_item = CrudManager(EventSerie).read_item(session, eventserie_id)
    return eventserie_item


@evt.patch("/eventserie/{eventserie_id}", response_model=EventSerieReadExtra)
def update_eventserie(*, session: Session = Depends(get_session), eventserie_id: int, eventserie: EventSerieUpdate):
    eventserie_item = CrudManager(EventSerie).edit_item(session, eventserie_id, eventserie)
    return eventserie_item


@evt.delete("/eventserie/{eventserie_id}")
def delete_eventserie(*, session: Session = Depends(get_session), eventserie_id: int):
    return CrudManager(EventSerie).delete_item(session, eventserie_id)


@srv.post("/eventservices", response_model=EventServiceReadExtra)
def create_eventservice(*, session: Session = Depends(get_session), eventservice: EventServiceCreate):
    eventservice_item = CrudManager(EventService).create_item(session, eventservice)
    return eventservice_item


@srv.get("/eventservices", response_model=List[EventServiceRead])
def read_eventservices(*, session: Session = Depends(get_session), offset: int = 0, limit: int = Query(default=100, lte=100)):
    eventservice = CrudManager(EventService).read_items(session, offset, limit)
    return eventservice


@srv.get("/eventservice/{eventservice_id}", response_model=EventServiceReadExtra)
def read_eventservice(*, session: Session = Depends(get_session), eventservice_id: int):
    eventservice_item = CrudManager(EventService).read_item(session, eventservice_id)
    return eventservice_item


@srv.patch("/eventservice/{eventservice_id}", response_model=EventServiceReadExtra)
def update_eventservice(*, session: Session = Depends(get_session), eventservice_id: int, eventservice: EventServiceUpdate):
    eventservice_item = CrudManager(EventService).edit_item(session, eventservice_id, eventservice)
    return eventservice_item


@srv.delete("/eventservice/{eventservice_id}")
def delete_eventservice(*, session: Session = Depends(get_session), eventservice_id: int):
    return CrudManager(EventService).delete_item(session, eventservice_id)


@srv.post("/eventservice/{eventservice_id}/note/{note_id}", response_model=EventServiceReadExtra)
def add_event_service_note(*, session: Session = Depends(get_session), eventservice_id: int, note_id: int):
    db_evt = CrudManager(EventService).read_item(session, eventservice_id)
    if db_evt:
        db_note = CrudManager(Note).read_item(session, note_id)
        if db_note:
            db_evt.notes.append(db_note)
        db_evt = CrudManager(EventService).edit_item(session, eventservice_id, db_evt)
    return db_evt


@srv.delete("/eventservice/{eventservice_id}/note/{note_id}", response_model=EventServiceReadExtra)
def remove_note_from_event_service(*, session: Session = Depends(get_session), eventservice_id: int, note_id: int):
    db_evt = CrudManager(EventService).read_item(session, eventservice_id)
    if db_evt:
        for per in db_evt.notes:
            if per.id == note_id:
                db_evt.notes.remove(per)
                break
        db_evt = CrudManager(Event).edit_item(session, eventservice_id, db_evt)
    return db_evt


@srv.post("/eventservice/{eventservice_id}/person/{person_id}", response_model=EventServiceReadExtra)
def add_associated_person_to_event_service(*, session: Session = Depends(get_session), eventservice_id: int, person_id: int):
    db_evt = CrudManager(EventService).read_item(session, eventservice_id)
    if db_evt:
        db_person = CrudManager(Person).read_item(session, person_id)
        if db_person:
            db_evt.associated_people.append(db_person)
        db_evt = CrudManager(EventService).edit_item(session, eventservice_id, db_evt)
    return db_evt


@srv.delete("/eventservice/{eventservice_id}/person/{person_id}", response_model=EventServiceReadExtra)
def remove_associated_person_from_event_service(*, session: Session = Depends(get_session), eventservice_id: int, person_id: int):
    db_evt = CrudManager(EventService).read_item(session, eventservice_id)
    if db_evt:
        for per in db_evt.associated_people:
            if per.id == person_id:
                db_evt.associated_people.remove(per)
                break
        db_evt = CrudManager(Event).edit_item(session, eventservice_id, db_evt)
    return db_evt