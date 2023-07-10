from sqlalchemy.orm import Session

from . import models, schemas


def create_url(db: Session, url: schemas.UrlForm):
    url_short = models.Url(original_url=url.url)
    db.add(url_short)
    db.commit()
    db.refresh(url_short)
    return url_short


def get_url(db: Session, url: int):
    return db.query(models.Url).filter(models.Url.short_url == url).first()
