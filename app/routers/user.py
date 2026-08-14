from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.user import (
    UserCreate,
    UserResponse,
    UserLogin,
    UserUpdate,
    ChangePassword,
    ForgotPassword,
    ResetPassword
)
from app.services.user_service import register_user , user_login , update_profile, change_password ,create_reset_token , reset_password
from app.auth.dependencies import get_current_user


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def register(
    data: UserCreate,
    db: Session = Depends(get_db)
):

    user = register_user(
        db=db,
        data=data
    )

    return user

@router.post("/login")
def login(
    data:UserLogin,
    db : Session = Depends(get_db)
    ):

    user = user_login(db , data)

    return user



@router.get("/profile",
            response_model=UserResponse)
def get_profile(current_user  =  Depends(get_current_user)):
    return current_user


@router.put("/update",
            response_model=UserResponse
            )
def updated_user(data : UserUpdate,
                 db : Session = Depends(get_db),
                 current_user = Depends(get_current_user)):

    return update_profile(
        db,
        current_user,
        data
    )

@router.put("/change-password")
def change_user_password(
    data  : ChangePassword,
    user = Depends(get_current_user),
    db : Session = Depends(get_db),
):
    return change_password(
           db,
           user,
           data
       )
    



@router.post("/forgot-password")
async def forgot_password(
    data: ForgotPassword,
    db: Session = Depends(get_db)
):

    return await create_reset_token(
        db,
        data.email
    )



@router.post("/reset-password")
def reset_password_api(
    data: ResetPassword,
    db: Session = Depends(get_db)
):

    return reset_password(
        db,
        data
    )
