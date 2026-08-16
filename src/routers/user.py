from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..db.deps import get_db
from ..crud.user import user_crud
from ..crud.user import user_crud


router = APIRouter(
    prefix="/user",
    tags=["users"]
)


@router.get("/users/", tags=["users"])
async def read_users(db: Session = Depends(get_db)):
    return user_crud.get_all(db)
