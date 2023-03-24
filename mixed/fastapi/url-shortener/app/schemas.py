from fastapi import Form
from pydantic import BaseModel, HttpUrl


class UrlForm(BaseModel):
    url: HttpUrl

    @classmethod
    def form(cls, url: HttpUrl = Form(...)):
        return cls(url=url)


class UrlShort(BaseModel):
    short_url: int
    original_url: HttpUrl

    class Config:
        orm_mode = True
