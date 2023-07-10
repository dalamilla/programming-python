from sqlalchemy import Column, Integer, String

from .db import Base


class Url(Base):
    __tablename__ = "url"

    short_url = Column(Integer, primary_key=True, index=True)
    original_url = Column(String, index=True)
