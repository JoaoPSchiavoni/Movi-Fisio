from fastapi import APIRouter, Depends, HTTPException, status
from src.models import User
from src.dependencies import get_db, hash_password
from src.schemas import UserSchema
from sqlalchemy.orm import Session

router = APIRouter(prefix="/auth", tags=["auth"])

@router.get("/")
async def read_auth():
    return {"auth": "auth"}


@router.post("/register")
async def register(user_data: UserSchema, session: Session = Depends(get_db)):
    existing_user = session.query(User).filter(User.email == user_data.email).first()
    if existing_user:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists")
    try:      
        hashed_pw = hash_password(user_data.password)    
        new_user = User(
            email=user_data.email, 
            password=hashed_pw, 
            name=user_data.name, cpf=user_data.cpf, 
            phone=user_data.phone, 
            lgpd_accepted=user_data.lgpd_accepted
            )
        session.add(new_user)
        session.commit()
        return HTTPException(status_code=status.HTTP_201_CREATED, detail="User created")
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))