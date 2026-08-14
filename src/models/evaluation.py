from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Numeric, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..db.base import Base


if TYPE_CHECKING:
    from .session import Session


class Evaluation(Base):
    __tablename__ = "evaluations"

    id: Mapped[int] = mapped_column(primary_key=True)
    session_id: Mapped[int] = mapped_column(ForeignKey("sessions.id"), unique=True, nullable=False, )
    overall_score: Mapped[Decimal] = mapped_column(Numeric(5, 2), nullable=False, )
    structure_score: Mapped[Decimal] = mapped_column( Numeric(5, 2), nullable=False, )
    math_score: Mapped[Decimal] = mapped_column( Numeric(5, 2), nullable=False, )
    business_reasoning_score: Mapped[Decimal] = mapped_column( Numeric(5, 2), nullable=False, )
    communication_score: Mapped[Decimal] = mapped_column( Numeric(5, 2), nullable=False, )
    strengths: Mapped[str] = mapped_column( Text, nullable=False, )
    weaknesses: Mapped[str] = mapped_column( Text, nullable=False, )
    feedback: Mapped[str] = mapped_column( Text, nullable=False, )

    session: Mapped["Session"] = relationship(back_populates="evaluation")

