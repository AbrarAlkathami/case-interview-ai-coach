from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer, String, Text, DateTime, func
from sqlalchemy.orm import mapped_column, Mapped, relationship

from ..db.base import Base


if TYPE_CHECKING:
    from .session import Session


class Message(Base):
    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(primary_key=True)
    session_id: Mapped[int] = mapped_column(ForeignKey("sessions.id"), nullable=False, index=True)
    role: Mapped[str] = mapped_column(String(50), nullable=False,)
    content: Mapped[str] = mapped_column(Text, nullable=False,)
    created_at: Mapped[datetime] = mapped_column( DateTime(timezone=True),server_default=func.now(),nullable=False, )
    sequence_number: Mapped[int] = mapped_column(Integer,nullable=False)

    session: Mapped["Session"] = relationship(back_populates="messages")
