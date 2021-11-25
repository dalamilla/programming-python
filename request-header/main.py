from fastapi import FastAPI, Request, Header
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*"
)

@app.get("/api/whoami")
async def whoami(request: Request, user_agent: str = Header(None), accept_language: str = Header(None)):
    client_host = request.client.host
    return {"ipaddress": client_host, "language": accept_language, "software": user_agent}
