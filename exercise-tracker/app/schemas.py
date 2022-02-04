from datetime import date, datetime
from fastapi import Form
from pydantic import BaseModel, Field, validator
from typing import Any, List, Optional


class UserCreate(BaseModel):
    username: str

    @classmethod
    def form(cls, username: str = Form(...)):
        return cls(username=username)


class User(BaseModel):
    id: str = Field(..., alias="_id")
    username: str

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class ExerciseBase(BaseModel):
    description: str
    duration: int
    date: date


class ExerciseCreate(ExerciseBase):
    @classmethod
    def form(
        cls,
        description: str = Form(...),
        duration: int = Form(...),
        date: Optional[str] = Form(None),
    ):
        return cls(description=description, duration=duration, date=date)

    @validator("date", pre=True)
    def parse_date(cls, value):
        if value is None:
            return date.today()
        for valid_fmt in ("%Y-%m-%d", "%a %b %d %Y"):
            try:
                return datetime.strptime(value, valid_fmt).date()
            except ValueError:
                pass
        raise ValueError("invalid date format")


class Exercise(ExerciseBase):

    id: str = Field(..., alias="_id")
    username: str
    date: str

    @classmethod
    def from_orm(cls, obj: Any) -> "Exercise":
        obj.date = obj.date.strftime("%a %b %d %Y")
        if hasattr(obj, "user"):
            obj.username = obj.user.username
            obj.id = obj.user.id
        return super().from_orm(obj)

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class ExerciseBaseLogs(ExerciseBase):
    date: str

    @classmethod
    def from_orm(cls, obj: Any) -> "ExerciseBaseLogs":
        obj.date = obj.date.strftime("%a %b %d %Y")
        return super().from_orm(obj)

    class Config:
        orm_mode = True


class UserLogs(User):
    count: int
    log: List[ExerciseBaseLogs]
