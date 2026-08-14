from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import DateTime, String, func

from ..db.base import Base


if TYPE_CHECKING:
    from .session import Session


class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(128), nullable=False)
    email: Mapped[str] = mapped_column (String(128), nullable=False, unique=True)
    password_hash: Mapped[str] = mapped_column(String(255),nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    sessions: Mapped[list["Session"]] = relationship(back_populates="user")


# # create the model in the db
# Base.metadata.create_all(engine)

# # create users in users table
# user1 = User(name="Abrar", email= "abrar.alkathami@gmail.com")
# user2 = User(name="Sara", email= "sara.althobaiti@gmail.com")


# # get users by filtering 
# user = session.query(User).filter_by(name='sara')

# #delete user
# session.delete(user)

# #colse the connection
# session.commit()