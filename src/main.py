from pydantic._internal import _forward_ref
from fastapi import FastAPI
from .auth_routes import router as auth_router
from .schedule_routes import router as schedule_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(schedule_router)

@app.get("/")
async def read_root():
    return {"Hello": "World"}
