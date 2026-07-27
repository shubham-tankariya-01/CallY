from sqlalchemy import Column, String, DateTime, Boolean
import uuid
from sqlalchemy.sql import func
from .base import Base

class Meeting(Base):
    __tablename__ = "meetings"

    id = Column(String,primary_key=True, default=lambda: str(uuid.uuid4()))
    room_code = Column(String, unique=True , nullable=False , index=True)
    created_at = Column(DateTime(timezone=True),nullable=False ,server_default=func.now())
    is_active = Column(Boolean,nullable=False, default=True)