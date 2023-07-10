from datetime import date
from typing import List

from fastapi import Depends, FastAPI, Query, Request
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates

from sqlalchemy.orm import Session

from . import crud, schemas, models
from .db import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins="*")

templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
async def main(request: Request):
    title = "Exercise Tracker"
    return templates.TemplateResponse("form.j2", {"request": request, "title": title})


@app.get("/api/users", response_model=List[schemas.User])
async def get_users(db: Session = Depends(get_db)):
    users = crud.get_users(db)
    return users


@app.post("/api/users", response_model=schemas.User)
async def create_user(
    user: schemas.UserCreate = Depends(schemas.UserCreate.form),
    db: Session = Depends(get_db),
):
    # this validation doesn't work with freecodecamp.
    # db_user = crud.get_user(db, user=user)
    # if db_user:
    #  raise HTTPException(status_code=400, detail="Username exist")
    return crud.create_user(db=db, user=user)


@app.get("/api/users/{username_id}/logs", response_model=schemas.UserLogs)
async def get_user_logs(
    username_id: int,
    limit: int = Query(None),
    from_date: date = Query(None, alias="from"),
    to_date: date = Query(None, alias="to"),
    db: Session = Depends(get_db),
):
    user = crud.get_user_by_id(db=db, username_id=username_id)
    logs = crud.get_user_logs(
        db=db,
        username_id=username_id,
        limit=limit,
        from_date=from_date,
        to_date=to_date,
    )
    return schemas.UserLogs(**user.__dict__, count=len(logs), log=logs)


@app.post("/api/users/{username_id}/exercises", response_model=schemas.Exercise)
async def create_user_exercise(
    username_id: int,
    exercise: schemas.ExerciseCreate = Depends(schemas.ExerciseCreate.form),
    db: Session = Depends(get_db),
):
    return crud.create_user_exercise(db=db, exercise=exercise, username_id=username_id)
