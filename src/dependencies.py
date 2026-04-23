from src.models import db
from sqlalchemy.orm import sessionmaker

def get_db():
    try:
        Session = sessionmaker(bind=db)
        session = Session()
        yield session
    finally:
        session.close()