from typing import Any, List
from fastapi import HTTPException, status
from pydantic import EmailStr
from sqlmodel import Session, select
from . import models, schemas
from app.core.session import commit_transaction


def get_person_by_id(db: Session, person_id: int) -> models.Person:
    stmt = select(models.Person).where(models.Person.id == person_id)
    person = db.exec(stmt).first()
    if not person:
        raise HTTPException(status_code=404, detail="Person not found")
    return person


def get_note_by_id(db: Session, note_id: int) -> models.Note:
    stmt = select(models.Note).where(models.Note.id == note_id)
    item = db.exec(stmt).first()
    if not item:
        raise HTTPException(status_code=404, detail="Note not found")
    return item


def get_businesshour_by_id(db: Session, hour_id: int) -> models.BusinessHour:
    stmt = select(models.BusinessHour).where(models.BusinessHour.id == hour_id)
    item = db.exec(stmt).first()
    if not item:
        raise HTTPException(status_code=404, detail="BusinessHour not found")
    return item


def get_person_by_email(db: Session, email: EmailStr) -> schemas.PersonRead:
    stmt = select(models.Person).where(models.Person.personal_email == email)
    item = db.exec(stmt).first()
    if not item:
        raise HTTPException(status_code=404, detail="Person not found")
    return item


def get_persons(db: Session, skip: int = 0, limit: int = 100) -> List[schemas.PersonRead]:
    return db.query(models.Person).offset(skip).limit(limit).all()


def create_person(db: Session, person: schemas.PersonCreate):
    db_person = models.Person(
        first_name=person.first_name,
        last_name=person.last_name,
        personal_email=person.personal_email,
        birth_date=person.birth_date,
        middle_name=person.middle_name,
    )
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person


def delete_person(db: Session, person_id: int):
    person = get_person_by_id(db, person_id)
    if not person:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Person not found")
    db.delete(person)
    db.commit()
    return person


def edit_person(db: Session, person_id: int, person: schemas.PersonUpdate) -> schemas.PersonRead:
    db_person = get_person_by_id(db, person_id)
    prep_person = prepare_for_update(person, db_person)
    commit_transaction(db, prep_person)
    return prep_person


def get_hours(db: Session, skip: int = 0, limit: int = 100) -> List[schemas.BusinessHourRead]:
    return db.query(models.BusinessHour).offset(skip).limit(limit).all()


def edit_business_hour(db: Session, hour_id: int, hour: schemas.BusinessHourUpdate) -> schemas.BusinessHourRead:
    db_hour = get_businesshour_by_id(db, hour_id)
    prep_item = prepare_for_update(hour, db_hour)
    commit_transaction(db, prep_item)
    return prep_item


def get_notes(db: Session, skip: int = 0, limit: int = 100) -> List[schemas.NoteRead]:
    return db.query(models.Note).offset(skip).limit(limit).all()


def edit_note(db: Session, note_id: int, note: schemas.NoteUpdate) -> schemas.NoteRead:
    db_note = get_note_by_id(db, note_id)
    prep_item = prepare_for_update(note, db_note)
    commit_transaction(db, prep_item)
    return prep_item


def get_receipt_by_id(db: Session, receipt_id: int) -> models.ConfirmationReceipt:
    stmt = select(models.ConfirmationReceipt).where(models.ConfirmationReceipt.id == receipt_id)
    receipt = db.exec(stmt).first()
    if not receipt:
        raise HTTPException(status_code=404, detail="Receipt not found")
    return receipt


def get_receipts(db: Session, skip: int = 0, limit: int = 100) -> List[schemas.ConfirmationRecieptRead]:
    receipts = db.query(models.ConfirmationReceipt).offset(skip).limit(limit).all()
    return receipts


def edit_receipt(db: Session, receipt_id: int, receipt: schemas.ConfirmationRecieptUpdate) -> schemas.ConfirmationRecieptRead:
    db_edit_receipt = get_receipt_by_id(db, receipt_id)
    prep_item = prepare_for_update(receipt, db_edit_receipt)
    commit_transaction(db, prep_item)
    return prep_item


def get_audience_by_id(db: Session, audience_id: int) -> models.Audience:
    stmt = select(models.Audience).where(models.Audience.id == audience_id)
    audience = db.exec(stmt).first()
    if not audience:
        raise HTTPException(status_code=404, detail="Audience not found")
    return audience


def get_audience(db: Session, skip: int = 0, limit: int = 100) -> List[schemas.AudienceRead]:
    audience = db.query(models.Audience).offset(skip).limit(limit).all()
    return audience


def edit_audience(db: Session, audience_id: int, audience: schemas.AudienceUpdate) -> schemas.AudienceRead:
    db_audience = get_audience_by_id(db, audience_id)
    prep_item = prepare_for_update(audience, db_audience)
    commit_transaction(db, prep_item)
    return prep_item


def get_orgtype_by_id(db: Session, org_type_id: int) -> models.OrganizationType:
    stmt = select(models.OrganizationType).where(models.OrganizationType.id == org_type_id)
    org_type = db.exec(stmt).first()
    if not org_type:
        raise HTTPException(status_code=404, detail="OrganizationType not found")
    return org_type


def get_orgtype(db: Session, skip: int = 0, limit: int = 100) -> List[schemas.OrganizationTypeRead]:
    org_type = db.query(models.OrganizationType).offset(skip).limit(limit).all()
    return org_type


def edit_orgtype(db: Session, org_type_id: int, org_type: schemas.OrganizationTypeUpdate) -> schemas.OrganizationTypeRead:
    db_org_type = get_orgtype_by_id(db, org_type_id)
    prep_item = prepare_for_update(org_type, db_org_type)
    commit_transaction(db, prep_item)
    return prep_item


def get_organization_by_id(db: Session, organization_id: int) -> models.Organization:
    stmt = select(models.Organization).where(models.Organization.id == organization_id)
    organization = db.exec(stmt).first()
    if not organization:
        raise HTTPException(status_code=404, detail="Organization not found")
    return organization


def get_organization(db: Session, skip: int = 0, limit: int = 100) -> List[schemas.OrganizationRead]:
    organization = db.query(models.Organization).offset(skip).limit(limit).all()
    return organization


def edit_organization(db: Session, organization_id: int, organization: schemas.OrganizationUpdate) -> schemas.OrganizationRead:
    db_organization = get_organization_by_id(db, organization_id)
    prep_item = prepare_for_update(organization, db_organization)
    commit_transaction(db, prep_item)
    return prep_item


def get_timeline_event_by_id(db: Session, timeline_event_id: int) -> models.TimeLineEvent:
    stmt = select(models.TimeLineEvent).where(models.TimeLineEvent.id == timeline_event_id)
    timeline_event = db.exec(stmt).first()
    if not timeline_event:
        raise HTTPException(status_code=404, detail="TimelineEvent not found")
    return timeline_event


def get_timeline_event(db: Session, skip: int = 0, limit: int = 100) -> List[schemas.TimeLineEventRead]:
    timeline = db.query(models.TimeLineEvent).offset(skip).limit(limit).all()
    return timeline


def edit_timeline_event(db: Session, timeline_id: int, timeline: schemas.TimeLineEventUpdate) -> schemas.TimeLineEventRead:
    db_timeline = get_timeline_event_by_id(db, timeline_id)
    prep_item = prepare_for_update(timeline, db_timeline)
    commit_transaction(db, prep_item)
    return prep_item


def get_arrangement_by_id(db: Session, arrangement_id: int) -> models.Arrangement:
    stmt = select(models.Arrangement).where(models.Arrangement.id == arrangement_id)
    arrangement = db.exec(stmt).first()
    if not arrangement:
        raise HTTPException(status_code=404, detail="Arrangement not found")
    return arrangement


def get_arrangement(db: Session, skip: int = 0, limit: int = 100) -> List[schemas.ArrangementRead]:
    timeline = db.query(models.Arrangement).offset(skip).limit(limit).all()
    return timeline


def edit_arrangement(db: Session, arrangement_id: int, arrangement: schemas.ArrangementUpdate) -> schemas.ArrangementRead:
    db_arrangement = get_arrangement_by_id(db, arrangement_id)
    prep_item = prepare_for_update(arrangement, db_arrangement)
    commit_transaction(db, prep_item)
    return prep_item


def prepare_for_update(updater: Any, db_item: Any) -> Any:
    model_data = updater.dict(exclude_unset=True)
    for key, value in model_data.items():
        print(key, value)
        if key in db_item.__dict__:
            setattr(db_item, key, value)
    return db_item
