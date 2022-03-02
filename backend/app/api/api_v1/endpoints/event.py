from typing import List

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session
from app.core.session import get_sqlmodel_sesion as get_session
from app.arrangement.model.basemodels import EventSerie, Event, EventService, Article
from app.arrangement.schema.events import EventSerieRead, EventSerieReadExtra, EventSerieCreate, EventSerieUpdate
from app.arrangement.schema.events import EventRead, EventReadExtra, EventCreate, EventUpdate
from app.arrangement.schema.events import EventServiceRead, EventServiceReadExtra, EventServiceCreate, EventServiceUpdate
from app.arrangement.schema.events import ArticleRead, ArticleCreate, ArticleUpdate
from app.arrangement.factory import CrudManager

event_router = evt = APIRouter()


@evt.post("/articles", response_model=ArticleRead)
def create_articles(*, session: Session = Depends(get_session), article: ArticleCreate):
    article_item = CrudManager(Article).create_item(session, article)
    return article_item


@evt.get("/articles", response_model=List[ArticleRead])
def read_articles(*, session: Session = Depends(get_session), offset: int = 0, limit: int = Query(default=100, lte=100)):
    articles = CrudManager(Article).read_items(session, offset, limit)
    return articles


@evt.get("/article/{article_id}", response_model=ArticleRead)
def read_article(*, session: Session = Depends(get_session), article_id: int):
    article_item = CrudManager(Article).read_item(session, article_id)
    return article_item


@evt.patch("/article/{article_id}", response_model=ArticleRead)
def update_article(*, session: Session = Depends(get_session), article_id: int, article: ArticleUpdate):
    article_item = CrudManager(Article).edit_item(session, article_id, article)
    return article_item


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


@evt.post("/events", response_model=EventReadExtra)
def create_event(*, session: Session = Depends(get_session), event: EventCreate):
    event_item = CrudManager(Event).create_item(session, event)
    return event_item


@evt.get("/events", response_model=List[EventRead])
def read_event(*, session: Session = Depends(get_session), offset: int = 0, limit: int = Query(default=100, lte=100)):
    events = CrudManager(Event).read_items(session, offset, limit)
    return events


@evt.get("/event/{event_id}", response_model=EventReadExtra)
def read_event(*, session: Session = Depends(get_session), event_id: int):
    event_item = CrudManager(Event).read_item(session, event_id)
    return event_item


@evt.patch("/event/{event_id}", response_model=EventReadExtra)
def update_event(*, session: Session = Depends(get_session), event_id: int, event: EventUpdate):
    event_item = CrudManager(Event).edit_item(session, event_id, event)
    return event_item


@evt.post("/eventservices", response_model=EventServiceReadExtra)
def create_eventservice(*, session: Session = Depends(get_session), eventservice: EventServiceCreate):
    eventservice_item = CrudManager(EventService).create_item(session, eventservice)
    return eventservice_item


@evt.get("/eventservices", response_model=List[EventServiceRead])
def read_eventservices(*, session: Session = Depends(get_session), offset: int = 0, limit: int = Query(default=100, lte=100)):
    eventservice = CrudManager(EventService).read_items(session, offset, limit)
    return eventservice


@evt.get("/eventservice/{eventservice_id}", response_model=EventServiceReadExtra)
def read_eventservice(*, session: Session = Depends(get_session), eventservice_id: int):
    eventservice_item = CrudManager(EventService).read_item(session, eventservice_id)
    return eventservice_item


@evt.patch("/eventservice/{eventservice_id}", response_model=EventServiceReadExtra)
def update_eventservice(*, session: Session = Depends(get_session), eventservice_id: int, eventservice: EventServiceUpdate):
    eventservice_item = CrudManager(EventService).edit_item(session, eventservice_id, eventservice)
    return eventservice_item
