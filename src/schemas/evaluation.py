from decimal import Decimal
from pydantic import BaseModel, ConfigDict
from typing import Optional


class EvaluationCreate(BaseModel):
    session_id: int
    overall_score: Decimal
    structure_score: Decimal
    math_score: Decimal
    business_reasoning_score: Decimal
    communication_score: Decimal
    strengths: str
    weaknesses: str
    feedback: str


class EvaluationResponse(BaseModel):
    id: int
    session_id: int
    overall_score: Decimal
    structure_score: Decimal
    math_score: Decimal
    business_reasoning_score: Decimal
    communication_score: Decimal
    strengths: str
    weaknesses: str
    feedback: str

    model_config = ConfigDict(from_attributes=True)


class EvaluationUpdate(BaseModel):
    overall_score: Optional[Decimal] = None
    structure_score: Optional[Decimal] = None
    math_score: Optional[Decimal] = None
    business_reasoning_score: Optional[Decimal] = None
    communication_score: Optional[Decimal] = None
    strengths: Optional[str] = None
    weaknesses: Optional[str] = None
    feedback: Optional[str] = None