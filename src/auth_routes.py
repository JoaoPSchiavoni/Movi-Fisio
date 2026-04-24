from fastapi import APIRouter, Depends, HTTPException, status
from src.models import User
from src.dependencies import get_db, hash_password
from src.schemas import UserSchema, LoginSchema
from sqlalchemy.orm import Session

router = APIRouter(prefix="/auth", tags=["auth"])

def create_token(user: User):
    token = f"kdjask12kj3ksajd93u10lka{user.id}sjd1167"
    return token

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
    user = session.query(User).filter(User.email == user_data.email).first()
    #TODO verificar senha
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    elif user.active == False:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    elif user.is_admin == True:
        pass
    elif user.is_admin == False:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
    # if not check_password(user_data.password, user.password):
    #     raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    token = create_token(user)
    return {"token": token, "user": user}