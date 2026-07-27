from fastapi import APIRouter,Depends,HTTPException
from schemas.meeting import MeetingResponse
from models.meetings import Meeting
from utils.generate_roomcode import room_code
from sqlalchemy.orm import Session
from core.database import get_db_session

router = APIRouter()

@router.post("/",response_model=MeetingResponse)
async def create_meeting(db:Session = Depends(get_db_session) ):
    roomcode = room_code()
    print(roomcode)
    # if we have a same room-code by anychnace, we will change it ;)
    while db.query(Meeting).filter(Meeting.room_code == roomcode).first():
        roomcode = room_code()
    new_Meeting = Meeting(room_code = roomcode)
    db.add(new_Meeting)
    db.commit()
    db.refresh(new_Meeting)

    return new_Meeting


@router.get("/{room_code}",response_model=MeetingResponse)
async def get_meeting(room_code:str,db:Session = Depends(get_db_session)):
    room_code = room_code.upper()
    meeting = db.query(Meeting).filter(Meeting.room_code == room_code).first()
    if meeting:
        return meeting
    raise HTTPException(status_code=404, detail="Meeting not found")