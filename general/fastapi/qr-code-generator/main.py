from io import BytesIO

import pyqrcode

from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from asyncer import asyncify

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins="*")


def qrcode_generator(input_data: str, scale: int = 5) -> bytes:
    qrcode = pyqrcode.create(input_data)
    buffer = BytesIO()
    qrcode.png(buffer, scale=scale)
    return buffer.getvalue()


@app.get("/api/qrcode")
async def qrcode(response: Response, data: str):
    qrcode_bytes = await asyncify(qrcode_generator)(data)
    return Response(content=qrcode_bytes, media_type="image/png")
