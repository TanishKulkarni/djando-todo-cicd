from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.db.database import get_db

from app.schemas.auth import *

from app.services.auth_service import *

from app.core.dependencies import (
    get_current_user
)

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post("/register")
def register(
    request: RegisterRequest,
    db: Session = Depends(get_db)
):

    user = register_user(
        db,
        request.email,
        request.password,
        request.full_name
    )

    return {
        "message": "User created",
        "user_id": user.id
    }


@router.post("/login")
def login(
    request: LoginRequest,
    db: Session = Depends(get_db)
):

    token = login_user(
        db,
        request.email,
        request.password
    )

    if not token:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    return {
        "access_token": token,
        "token_type": "bearer"
    }


@router.get("/me")
def me(user=Depends(get_current_user)):
    return user