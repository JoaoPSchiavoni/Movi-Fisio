from fastapi import FastAPI
from dotenv import load_dotenv
from os import getenv

from src.auth_routes import router as auth_router
from src.schedule_routes import router as schedule_router

load_dotenv()

SECRET_KEY = getenv("SECRET_KEY")


app = FastAPI()

app.include_router(auth_router)
app.include_router(schedule_router)


@app.get("/")
async def read_root():
    return {"Hello": "World"}
