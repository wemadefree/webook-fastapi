from typing import Optional
from datetime import datetime
from pydantic import BaseModel
from sqlalchemy import Column, DateTime
from sqlmodel import Field
from app.core.utils import to_camel


class TimeStampMixin(BaseModel):
    """Provides last created/modified timestamps"""

    created: Optional[datetime] = Field(
        sa_column=Column(
            DateTime,
            default=datetime.utcnow,
            nullable=False,
        )
    )

    modified: Optional[datetime] = Field(
        sa_column=Column(
            DateTime,
            default=datetime.utcnow,
            onupdate=datetime.utcnow,
        )
    )


class CamelCaseMixin(BaseModel):

    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True

