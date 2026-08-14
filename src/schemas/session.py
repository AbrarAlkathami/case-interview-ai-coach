from datetime import datetime
from pydantic import BaseModel, EmailStr, Field, ConfigDict


class SessionCreate(BaseModel):
    user_id: int
    case_id: int
    status: str

class SessionResponse(BaseModel):
    id: int
    user_id: int
    case_id: int
    started_at: datetime
    completed_at: datetime | None
    status: str

    model_config = ConfigDict(from_attributes=True)

class SessionUpdate(BaseModel):
    completed_at: datetime | None
    status: str

