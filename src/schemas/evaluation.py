from decimal import Decimal

from pydantic import BaseModel, ConfigDict


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
    overall_score: Decimal | None = None
    structure_score: Decimal | None = None
    math_score: Decimal | None = None
    business_reasoning_score: Decimal | None = None
    communication_score: Decimal | None = None
    strengths: str | None = None
    weaknesses: str | None = None
    feedback: str | None = None