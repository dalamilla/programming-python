from datetime import date
from operator import and_
from sqlalchemy.orm import Session

from . import models, schemas


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(username=user.username)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, user: schemas.UserCreate):
    return db.query(models.User).filter(models.User.username == user.username).first()


def get_user_by_id(db: Session, username_id: int):
    return db.query(models.User).filter(models.User.id == username_id).first()


def get_users(
    db: Session,
    skip: int = 0,
):
    return db.query(models.User).offset(skip).all()


def create_user_exercise(
    db: Session, exercise: schemas.ExerciseCreate, username_id: int
):
    user_exercise = models.Exercise(**exercise.dict(), username_id=username_id)
    db.add(user_exercise)
    db.commit()
    db.refresh(user_exercise)
    return user_exercise


def get_user_logs(
    db: Session,
    username_id: int,
    from_date: date,
    to_date: date,
    skip: int = 0,
    limit: int = -1,
):
    if from_date is None and to_date is None:
        query = (
            db.query(models.Exercise)
            .filter(models.Exercise.username_id == username_id)
            .offset(skip)
            .limit(limit)
            .all()
        )
    elif from_date is None:
        query = (
            db.query(models.Exercise)
            .filter(models.Exercise.username_id == username_id)
            .filter(models.Exercise.date <= to_date)
            .offset(skip)
            .limit(limit)
            .all()
        )
    elif to_date is None:
        query = (
            db.query(models.Exercise)
            .filter(models.Exercise.username_id == username_id)
            .filter(models.Exercise.date >= from_date)
            .offset(skip)
            .limit(limit)
            .all()
        )
    else:
        query = (
            db.query(models.Exercise)
            .filter(models.Exercise.username_id == username_id)
            .filter(
                and_(models.Exercise.date >= from_date, models.Exercise.date <= to_date)
            )
            .offset(skip)
            .limit(limit)
            .all()
        )

    return query
