from fastapi import FastAPI
from models.base import Base
from core.database import engine
from api import meeting_api

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(meeting_api.router,prefix="/api/meeting",tags=["meeting"])

@app.get("/")
async def server()->dict[str,str]:
    return {"server" : "Running"}