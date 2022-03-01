from fastapi import HTTPException
from sqlmodel import Session, select
from typing import Any, List


class CrudManager:

    def __init__(self, class_model):
        self.class_model = class_model
        if not getattr(self.class_model.__config__, "table", False):
            raise ValueError("Not valid SQL model (table need to be set on True)")

    def create_item(self, session: Session, item: Any) -> Any:
        db_item = self.class_model.from_orm(item)
        session.add(db_item)
        session.commit()
        session.refresh(db_item)
        return db_item

    def read_item(self, session: Session, item_id: int) -> Any:
        return self._get_item_by_id(session, item_id)

    def read_items(self, session: Session, offset: int, limit: int) -> List[Any]:
        locations = session.query(self.class_model).offset(offset).limit(limit).all()
        return locations

    def edit_item(self, db: Session, item_id: int, item: Any) -> Any:
        db_item = self._get_item_by_id(db, item_id)
        prep_person = self._prepare_for_update(item, db_item)
        self._commit_transaction(db, prep_person)
        return prep_person

    def delete_item(self, session: Session, item_id: int) -> Any:
        db_item = self._get_item_by_id(session, item_id)
        if not db_item:
            raise HTTPException(status_code=404, detail=f"{self.class_model.__name__} not found")
        session.delete(db_item)
        session.commit()
        return {"ok": True}

    def _get_item_by_id(self, db: Session, item_id: int) -> Any:
        stmt = select(self.class_model).where(self.class_model.id == item_id)
        person = db.exec(stmt).first()
        if not person:
            raise HTTPException(status_code=404, detail=f"{self.class_model.__name__} not found")
        return person

    def _prepare_for_update(self, updater: Any, db_item: Any) -> Any:
        model_data = updater.dict(exclude_unset=True)
        for key, value in model_data.items():
            print(key, value)
            if key in db_item.__dict__:
                setattr(db_item, key, value)
        return db_item

    def _commit_transaction(self, session: Session, db_item: Any):
        """When adding or updating record in database (POST, PATCH, PUT)"""
        session.add(db_item)
        session.commit()
        session.refresh(db_item)
