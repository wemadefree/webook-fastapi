from app.core.session import Base
from sqlalchemy import Boolean, Column, Integer, String


class User(Base):
    __tablename__ = "users_user"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    first_name = Column(String)
    last_name = Column(String)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    person_id = Column(Integer, default=0)
