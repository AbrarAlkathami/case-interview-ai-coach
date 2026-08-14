from pydantic import BaseModel, ConfigDict
from typing import Any


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
    case_name: str | None = None
    case_type: str | None = None
    difficulty: str | None = None
    case_content: str | None = None
    structured_metadata: dict[str, Any] | None = None