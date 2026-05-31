from app.models.user import User

from app.repositories.auth_repository import (
    get_user_by_email,
    create_user
)

from app.core.security import (
    hash_password,
    verify_password,
    create_access_token
)


def register_user(
    db,
    email,
    password,
    full_name
):

    existing = get_user_by_email(
        db,
        email
    )

    if existing:
        raise Exception(
            "Email already registered"
        )

    user = User(
        email=email,
        password_hash=hash_password(password),
        full_name=full_name
    )

    create_user(db, user)

    return user


def login_user(
    db,
    email,
    password
):
    user = get_user_by_email(
        db,
        email
    )

    if not user:
        return None

    if not verify_password(
        password,
        user.password_hash
    ):
        return None

    token = create_access_token(
        {"sub": str(user.id)}
    )

    return token