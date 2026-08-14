from typing import TYPE_CHECKING, Any

from sqlalchemy import JSON, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..db.base import Base


if TYPE_CHECKING:
    from .session import Session


class Case(Base):
    __tablename__ = "cases"
    id: Mapped[int] = mapped_column(primary_key=True)

    case_name: Mapped[str] = mapped_column( String(255), nullable=False,)
    case_type: Mapped[str] = mapped_column( String(50), nullable=False,)
    difficulty: Mapped[str] = mapped_column( String(50), nullable=False,)
    case_content: Mapped[str] = mapped_column( Text, nullable=False,)
    structured_metadata: Mapped[dict[str, Any] | None] = mapped_column( JSON, nullable=True,)

    sessions: Mapped[list["Session"]] = relationship(back_populates="case")

