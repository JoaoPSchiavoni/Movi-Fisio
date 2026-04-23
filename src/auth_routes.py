from fastapi import APIRouter
from src.models import User, db
from sqlalchemy.orm import sessionmaker

router = APIRouter(prefix="/auth", tags=["auth"])

@router.get("/")
async def read_auth():
    return {"auth": "auth"}


@router.post("/register")
async def register(email:str, password:str, name:str, cpf:str, phone:str, lgpd_accepted:bool):
    Session = sessionmaker(bind=db)
    session = Session()
    user = session.query(User).filter(User.email == email).first()
    if user:
        return {"error": "User already exists"}
    try:
        if email and password and name and cpf and phone and lgpd_accepted:
            user = User(email=email, password=password, name=name, cpf=cpf, phone=phone, lgpd_accepted=lgpd_accepted)
            session.add(user)
            session.commit()
            return {"message": "User created"}
        return {"error": "Missing required fields"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        session.close()