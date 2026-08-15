from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from ..db.deps import get_db
from ..services.auth_service import auth_service
from ..core.auth import generate_access_token
from ..core.config import settings
from ..schemas.user import UserCreate, UserLogin, AuthResponse


router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)


@router.post("/register", response_model=AuthResponse)
async def register_user( user_data: UserCreate, db: Session = Depends(get_db)):

    user = await auth_service.register(db, user_data)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User already exists"
        )

    access_token = await generate_access_token(
        data={"sub": user.email},
        expires_delta=timedelta(
            minutes=settings.token_expires
        )
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": user,
    }


@router.post("/token", response_model=AuthResponse)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):

    user_data = UserLogin(
    email=form_data.username,
    password=form_data.password,
    )

    user = await auth_service.login(db, user_data)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password"
        )

    access_token = await generate_access_token(
        data={"sub": user.email},
        expires_delta=timedelta(
            minutes=settings.token_expires
        )
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": user,
    }