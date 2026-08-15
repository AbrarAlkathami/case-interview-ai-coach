from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..db.base import Base


if TYPE_CHECKING:
    from .user import User
    from .message import Message
    from .case import Case
    from .evaluation import Evaluation


class Session(Base):
    __tablename__ = "sessions"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False, index=True)
    case_id: Mapped[int] = mapped_column( ForeignKey('cases.id'), nullable=False, index=True)
    started_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    completed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    status: Mapped[str] = mapped_column(String(50), nullable=False)

    user: Mapped["User"] = relationship(back_populates="sessions")
    messages: Mapped[list["Message"]] = relationship( back_populates="session")
    case: Mapped["Case"]  = relationship(back_populates="sessions")
    evaluation: Mapped["Evaluation"] = relationship(back_populates="session")