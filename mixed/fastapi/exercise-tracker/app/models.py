from sqlalchemy import Column, Date, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from .db import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)

    exercise = relationship("Exercise", back_populates="user")


class Exercise(Base):
    __tablename__ = "exercise"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(Text)
    duration = Column(Integer)
    date = Column(Date)
    username_id = Column(Integer, ForeignKey("user.id"))

    user = relationship("User", back_populates="exercise")
