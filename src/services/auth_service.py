from sqlalchemy.orm import Session

from ..schemas.user import UserCreate
from ..schemas.auth import UserLogin
from ..utils.security import hash_pwd, check_pwd
from ..crud.user import user_crud
from ..models.user import User


class AuthService:
    async def register(self, db: Session, user_data: UserCreate) -> User | None:

        existing_user = user_crud.get_by_email(db, user_data.email)

        if existing_user:
            return None

        hashed_password = hash_pwd(user_data.password)
        user_dict = {
            "name": user_data.name,
            "email": user_data.email,
            "password_hash": hashed_password,
        }
        return user_crud.create(db, user_dict)
        

    async def login(self, db: Session, user_data: UserLogin) -> User | None:

        user = user_crud.get_by_email(db, user_data.email)

        if not user:
            return None

        if not check_pwd(user_data.password, user.password_hash):
            return None

        return user

auth_service = AuthService()