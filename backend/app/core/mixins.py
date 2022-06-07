from datetime import datetime
from pydantic import BaseModel
from sqlalchemy import Column, DateTime, String
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import validates
from slugify import slugify
from abc import ABC, abstractmethod

from app.core.utils import to_camel
from app.core.session import Base


class TimeStampMixin:
    """Provides last created/modified timestamps"""

    created = Column(DateTime, default=datetime.utcnow, nullable=False)
    modified = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class SlugifyNameMixin:
    """Provides slugs for model. By default it expect to slugify it by name"""
    slug = Column(String(100), nullable=False)

    @validates('name')
    def create_slug_by_name(self, key, value):
        self.slug = slugify(value)
        return value

    def update_slug(self, count: int = 0):
        self.slug = f"{self.get_stripped_slug()}-{count}"

    def get_stripped_slug(self, delimiter: str = '-'):
        """Return the last element from string, prior the delimiter

        If string ends in the delimiter or the delimiter is absent,
        returns the original string without the delimiter.

        """
        prefix, delim, last = self.slug.rpartition(delimiter)
        return prefix if (delim and last) else self.slug

    def get_slug_suffix(self, delimiter: str = '-') -> int:
        """Return the slug suffix from string, after the delimiter

        If string ends in the delimiter or the delimiter is absent,
        returns the original string without the delimiter.

        """
        try:
            prefix, delim, last = self.slug.rpartition(delimiter)
            print(prefix, delim, last, self.slug)
            if delim and last:
                return int(last)
            else:
                return 0
        except:
            return 0


class CamelModelMixin(BaseModel):

    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True

