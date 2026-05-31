from jose import jwt

from fastapi import Depends
from fastapi import HTTPException

from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.orm import Session

from app.db.database import get_db

from app.models.user import User

from app.core.config import settings


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="auth/login"
)


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):

    try:

        payload = jwt.decode(
            token,
            settings.JWT_SECRET,
            algorithms=[settings.JWT_ALGORITHM]
        )

        user_id = payload.get("sub")

        user = db.query(User).filter(
            User.id == user_id
        ).first()

        return user

    except:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )