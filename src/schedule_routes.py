from fastapi import APIRouter

router = APIRouter(prefix="/schedule", tags=["schedule"])

@router.get("/")
async def read_schedule():
    return {"schedule": "schedule"}