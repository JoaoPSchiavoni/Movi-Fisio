from pwdlib import PasswordHash
from fastapi import APIRouter, Depends, HTTPException, status
from src.models import User
from src.dependencies import get_db, hash_password, verify_password
from src.schemas import UserSchema, LoginSchema
from sqlalchemy.orm import Session

router = APIRouter(prefix="/auth", tags=["auth"])

def create_token(user: User):
    return f"kdjask12kj3ksajd93u10lka{user.id}sjd1167"

def auth_user(email, password, session: Session):
    user = session.query(User).filter(User.email == email).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciais inválidas")
    
    if not verify_password(password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciais inválidas")
        
    if not user.active:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Usuário inativo")
        
    # if not user.is_admin:
    #     raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Acesso restrito a administradores")
        
    return user

@router.get("/")
async def read_auth():
    return {"auth": "auth"}


@router.post("/register")
async def register(user_data: UserSchema, session: Session = Depends(get_db)):
    existing_user = session.query(User).filter(User.email == user_data.email).first()
    if existing_user:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists")
    try:
        user_dict = user_data.model_dump(exclude={"password", "admin"})
        hashed_pw = hash_password(user_data.password)

        new_user = User(**user_dict, password=hashed_pw)
        session.add(new_user)
        session.commit()
        return HTTPException(status_code=status.HTTP_201_CREATED, detail="User created")
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        
@router.post("/login")
async def login(user_data: LoginSchema, session: Session = Depends(get_db)):
    user = auth_user(user_data.email, user_data.password, session)
    token = create_token(user)
    return {"token": token, "user": {"email": user.email, "id": user.id}}