from src.models import db
from sqlalchemy.orm import sessionmaker
import hashlib
import bcrypt 

def get_db():
    try:
        Session = sessionmaker(bind=db)
        session = Session()
        yield session
    finally:
        session.close()

def hash_password(password: str) -> str:
    sha_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(sha_hash.encode('utf-8'), salt)

    return hashed_password.decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    sha_hash = hashlib.sha256(plain_password.encode('utf-8')).hexdigest()
    
    return bcrypt.checkpw(sha_hash.encode('utf-8'), hashed_password.encode('utf-8'))