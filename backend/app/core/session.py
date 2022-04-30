from typing import Any
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

from . import config

engine = create_engine(config.SQLALCHEMY_DATABASE_URI,)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependency
def get_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def commit_transaction(session: Session, db_item: Any):
    """When adding or updating record in database (POST, PATCH, PUT)"""
    session.add(db_item)
    session.commit()
    session.refresh(db_item)


