from typing import Optional
from datetime import datetime
from pydantic import BaseModel, root_validator
from sqlalchemy import Column, DateTime
from sqlmodel import Field
from slugify import slugify
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


class SlugifyMixin(BaseModel):
    """Provides slugs for model"""
    slug: Optional[str]

    @root_validator
    def create_slug(cls, values):
        name = values.get("name")
        slugify_name = slugify(name)
        values["slug"] = slugify_name
        return values


class CamelCaseMixin(BaseModel):

    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True

