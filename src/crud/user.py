from sqlalchemy import select
from sqlalchemy.orm import Session

from ..crud.base import CRUDBase
from ..models.user import User


class UserCRUD(CRUDBase[User]):
    def __init__(self):
        super().__init__(User)

    def get_by_email(self, db: Session, email: str) -> User | None:
        statement = select(User).where(User.email == email)
        return db.scalar(statement)


user_crud = UserCRUD()