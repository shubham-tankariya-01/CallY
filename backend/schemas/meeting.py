from pydantic import BaseModel,Field,ConfigDict
from uuid import UUID
from datetime import datetime

class MeetingResponse(BaseModel):
    meeting_id : UUID
    room_code : str = Field(min_length=7,max_length=7)
    created_at : datetime 
    ia_active : bool

    model_config = ConfigDict(from_attributes=True)