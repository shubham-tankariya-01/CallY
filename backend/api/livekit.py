from fastapi import APIRouter,HTTPException,Depends
from schemas.meeting import LiveKit_token
from sqlalchemy.orm import Session
from core.database import get_db_session
from models.meetings import Meeting
from livekit.api import AccessToken, VideoGrants
from core.config import settings


router = APIRouter()

@router.post("/token")
async def get_livekit_token(request: LiveKit_token, db: Session = Depends(get_db_session)):
    room_code = request.room_code.upper()
    meeting = db.query(Meeting).filter(Meeting.room_code == room_code).first()

    if not meeting:
        raise HTTPException(status_code=404 , detail="Meeting not found!")

    token = (
       AccessToken(api_key=settings.LIVEKIT_API_KEY, api_secret=settings.LIVEKIT_API_SECRET)
        .with_identity(request.id)
        .with_name(request.participant_name)
        .with_grants(VideoGrants(
            room_join=True,
            room=request.room_code.upper(),
            can_publish=True,
            can_subscribe=True,
            can_publish_data=True,
        ))
    )

    return {
        "token": token.to_jwt(),
        "url": settings.LIVEKIT_URL,
        "name" : request.participant_name,
        "room_code" : request.room_code,
    }

    
