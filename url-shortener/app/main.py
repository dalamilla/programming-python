from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from sqlalchemy.orm import Session

from . import crud, schemas, models
from .db import engine, get_db
from .utils import check_domain

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins="*")


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(exc.detail, status_code=exc.status_code)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    if "short_url" in request.path_params:
        return JSONResponse({"error": "Wrong format"}, status_code=200)
    return JSONResponse({"error": "invalid url"}, status_code=200)


@app.post("/api/shorturl", response_model=schemas.UrlShort)
async def create_shorturl(
    url: schemas.UrlForm = Depends(schemas.UrlForm.form),
    db: Session = Depends(get_db),
):
    if not check_domain(url.url.host):
        raise HTTPException(status_code=200, detail={"error": "Invalid Hostname"})
    return crud.create_url(db, url=url)


@app.get("/api/shorturl/{short_url}")
async def get_shorturl(short_url: int, db: Session = Depends(get_db)):
    url = crud.get_url(db=db, url=short_url)
    if url is None:
        raise HTTPException(
            status_code=200, detail={"error": "No short URL found for the given input"}
        )
    return RedirectResponse(url.original_url, status_code=302)
