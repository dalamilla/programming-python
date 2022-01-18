from typing import Union
from datetime import datetime, timezone

from fastapi import FastAPI, Response, status
from fastapi.param_functions import Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*"
)

def parsing_date(str_date: str):

    for valid_fmt in ('%Y-%m-%d', '%d %B %Y', '%d %B %Y, %Z'):
        try:
            pars_date = datetime.strptime(str_date, valid_fmt)
            return pars_date.replace(tzinfo=timezone.utc)
        except ValueError:
            pass

    raise ValueError('invalid date format')

@app.get("/api")
@app.get("/api/{input_date}")
async def root(response: Response, input_date: Union[int, str] = Query(None)):

    if input_date is None:
        time_date = datetime.now(timezone.utc)
    elif isinstance(input_date, int):
        time_date = datetime.fromtimestamp(input_date/1000, tz=timezone.utc)
    else:
        try:
            time_date = parsing_date(input_date)
        except ValueError:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {'error': 'Invalid Date'}

    unix = int(time_date.timestamp() * 1000)
    utc = time_date.strftime('%a, %d %b %Y %H:%M:%S GMT')
    return {"unix": unix, "utc": utc}
