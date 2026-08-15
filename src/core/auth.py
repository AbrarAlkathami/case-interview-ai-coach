from datetime import datetime, timedelta
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from typing import Optional
import jwt
from sqlalchemy.orm import Session
from ..core.config import settings
from ..db.deps import get_db
from ..schemas.user import TokenData
from ..crud.user import user_crud

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")


async def generate_access_token(data: dict, expires_delta: Optional[timedelta]=None):
    to_encode = data.copy()
    if expires_delta:
       expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(minutes=30)
    to_encode.update({"exp":expire})    
    encodeed_jwt = jwt.encode(to_encode, settings.secret_key, settings.algorithm)

    return encodeed_jwt


async def verify_token(token: str) -> TokenData:
    try:
        payload = jwt.decode(
            token,
            settings.secret_key,
            algorithms=[settings.algorithm]
        )
        email: str = payload.get("sub")
        if email is None:
            raise HTTPException(
                status_code = status.HTTP_401_UNAUTHORIZED,
                detail = "Could not verify credentials",
                headers={"WWW-Authenticate":"Bearer"}
            )
        return TokenData(email=email)
    except jwt.PyJWTError:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "Could not verify credentials",
            headers={"WWW-Authenticate":"Bearer"}
        )

async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    token_data = verify_token(token)
    user = user_crud.get_by_email(db, token_data.email)
    if user is None:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "User does not exist",
            headers={"WWW-Authenticate":"Bearer"}
        )
    return user