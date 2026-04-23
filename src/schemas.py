from pydantic import BaseModel, EmailStr
from typing import Optional

class UserSchema(BaseModel):
    email: EmailStr
    password: str
    name: str
    cpf: str
    phone: str
    lgpd_accepted: bool
    admin: Optional[bool] = False

class LoginSchema(BaseModel):
    email: EmailStr
    password: str