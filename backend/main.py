from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.base import Base
from core.database import engine
from api import meeting_api,livekit

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Trusts requests from Vite
    allow_credentials=True,
    allow_methods=["*"],                      # Allows OPTIONS, POST, GET, etc.
    allow_headers=["*"],                      # Allows Content-Type and other headers
)

app.include_router(meeting_api.router,prefix="/api/meeting",tags=["meeting"])
app.include_router(livekit.router,prefix="/api/livekit",tags=["livekit"])

@app.get("/")
async def server()->dict[str,str]:
    return {"server" : "Running"}