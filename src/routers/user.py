from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..core.auth import get_current_user
from ..db.deps import get_db
from ..schemas.user import UserResponse
from ..crud.user import user_crud
from ..crud.user import user_crud
from ..models.user import User


router = APIRouter(
    prefix="/user",
    tags=["users"]
)


@router.get("/users/", tags=["users"])
async def read_users(db: Session = Depends(get_db)):
    return user_crud.get_all(db)


@router.get("/me", response_model=UserResponse)
async def get_me( current_user: User = Depends(get_current_user)):
    return current_user