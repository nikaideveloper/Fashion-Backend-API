from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer

from app.auth.jwt import verify_token
from app.crud.user import get_user_by_email , get_user_by_id
from app.database import get_db

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="login"
)


def get_current_user(token :str=Depends(oauth2_scheme), db : Session = Depends(get_db)):

    payload  = verify_token(token)

    if not payload :

        raise HTTPException(
            status_code="401",
            detail="Invalid token"
        )


    user_id = payload.get("sub")

    if not user_id:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )

    user = get_user_by_id(db , user_id)

    if not user :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    if not user.is_active :
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Account is inactive"
        )

    return user

    


   
