from datetime import datetime
from pydantic import BaseModel, ConfigDict


class MessageCreate(BaseModel):
    session_id: int
    role: str
    content: str


class MessageResponse(BaseModel):
    id: int
    session_id: int
    role: str
    content: str
    created_at: datetime
    sequence_number: int

    model_config = ConfigDict(from_attributes=True)


class MessageUpdate(BaseModel):
    content: str


