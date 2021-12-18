from typing import Optional
from fastapi import FastAPI, File, UploadFile, Header, Request
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*"
)

templates = Jinja2Templates(directory="templates")

@app.post("/api/fileanalyse")
async def file_analyse(upfile: UploadFile = File(...), content_length: Optional[str] = Header(None)):
    return {"name": upfile.filename, "type": upfile.content_type, "size": content_length}

@app.get("/", response_class=HTMLResponse)
async def main(request: Request):
    title = "Form File"
    return templates.TemplateResponse("form.j2", {"request": request, "title": title})
