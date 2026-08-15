from pydantic import BaseModel, ConfigDict
from typing import Any, Optional


class CaseCreate(BaseModel):
    case_name: str
    case_type: str
    difficulty: str
    case_content: str
    structured_metadata: dict[str, Any]



class CaseResponse(BaseModel):
    id: int
    case_name: str
    case_type: str
    difficulty: str
    case_content: str
    structured_metadata: dict[str, Any]

    model_config = ConfigDict(from_attributes=True)


class CaseUpdate(BaseModel):
    case_name: Optional[str] = None
    case_type: Optional[str]  = None
    difficulty: Optional[str]  = None
    case_content: Optional[str]  = None
    structured_metadata: Optional[dict[str, Any]] = None