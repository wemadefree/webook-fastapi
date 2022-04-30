from datetime import datetime
from pydantic import BaseModel
from sqlalchemy import Column, DateTime, String
from sqlalchemy.orm import validates
from slugify import slugify

from app.core.utils import to_camel
from app.core.session import Base


class TimeStampMixin:
    """Provides last created/modified timestamps"""

    created = Column(DateTime, default=datetime.utcnow, nullable=False)
    modified = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class SlugifyMixin:
    """Provides slugs for model. By default it expect to slugify it by name"""
    slug = Column(String(100), nullable=False)

    @validates('name')
    def update_slug(self, key, name):
        self.slug = slugify(name)
        return self.slug


class CamelModelMixin(BaseModel):

    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True

