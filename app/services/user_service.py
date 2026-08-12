from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.crud.user import get_user_by_email , create_user
from app.auth.password import hash_password
from app.schemas.user import UserCreate


def register_user(
    db: Session,
    data: UserCreate
):

    # 1. Check existing user

    existing_user = get_user_by_email(
        db,
        data.email
    )

    if existing_user:

        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered"
        )

    # 2. Hash password

    hashed_password = hash_password(
        data.password
    )

    # 3. Create user

    user = create_user(
        db=db,
        name=data.name,
        email=data.email,
        password_hash=hashed_password
    )

    return user