from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from datetime import datetime, timedelta, timezone
import secrets

from app.crud.user import get_user_by_email , create_user , update_user
from app.auth.password import hash_password,verify_password
from app.auth.jwt import create_access_token
from app.schemas.user import UserCreate , UserLogin , UserUpdate , ChangePassword , ResetPassword ,ForgotPassword
from app.services.email_service import send_reset_email
from app.models.user import User


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


def user_login(db : Session , data : UserLogin ):

    user = get_user_by_email(db,data.email)

    if not user :

        raise HTTPException(
            status_code=404,
            detail="Invalid email or password"
        )

    password_correct = verify_password(data.password , user.password_hash)

    if not password_correct :
        raise HTTPException(
                    status_code=401,
                    detail="Invalid  password"
                )

    if not user.is_active :

        raise HTTPException(
            status_code=403,
            detail="Account is inactive"
        )

    access_token = create_access_token(
        user_id=user.id,
        email=user.email,
        role=user.role
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }



def update_profile(
        db : Session,
        user,
        data : UserUpdate
):
     
     if data.name is not None:

        user.name = data.name

     if data.email is not None:

        existing_user = get_user_by_email(
            db,
            data.email
        )

        if (existing_user and existing_user.id != user.id):

            raise HTTPException(
                status_code=409,
                detail="Email already registered"
            )

        user.email = data.email

     

     return update_user(
        db,
        user
    )


def change_password(
        db : Session,
        user ,
        data : ChangePassword
):
    correct = verify_password(
        data.current_password,
        user.password_hash
    )

    if not correct :
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Current password is incorrect"
        )

    user.password_hash = hash_password(
        data.new_password
    )

    update_user(
        db,
        user
    )

    return {
        "message": "Password changed successfully"
    }





async def create_reset_token(
    db,
    email: str
):

    user = get_user_by_email(
        db,
        email
    )

    # Don't reveal whether email exists
    if not user:

        return {
            "message": (
                "If the email exists, "
                "a reset link has been sent"
            )
        }

    # Generate token
    token = secrets.token_urlsafe(32)

    # Save token
    user.reset_token = token

    # Token valid for 15 minutes
    user.reset_token_expires = (
        datetime.now(timezone.utc)
        + timedelta(minutes=15)
    )

    update_user(
        db,
        user
    )

    # Send email
    await send_reset_email(
        email=user.email,
        reset_token=token
    )

    return {
        "message": (
            "If the email exists, "
            "a reset link has been sent"
        )
    }


def reset_password(
    db: Session,
    data: ResetPassword
):

    user = (
        db.query(User)
        .filter(User.reset_token == data.token)
        .first()
    )

    if not user:

        raise HTTPException(
            status_code=400,
            detail="Invalid reset token"
        )

    now = datetime.now(timezone.utc)

    if (
        not user.reset_token_expires
        or user.reset_token_expires < now
    ):

        raise HTTPException(
            status_code=400,
            detail="Reset token expired"
        )

    user.password_hash = hash_password(
        data.new_password
    )

    user.reset_token = None
    user.reset_token_expires = None

    update_user(
        db,
        user
    )

    return {
        "message": "Password reset successfully"
    }