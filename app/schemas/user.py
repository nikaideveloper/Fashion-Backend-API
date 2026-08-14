from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str



class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: str
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class UserLogin(BaseModel):
    email : EmailStr
    password : str


class UserUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None


class ChangePassword(BaseModel):
      current_password: str
      new_password: str



class ForgotPassword(BaseModel):

    email: EmailStr


class ResetPassword(BaseModel):

    token: str
    new_password: str