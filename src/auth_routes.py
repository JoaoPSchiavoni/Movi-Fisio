from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["auth"])

@router.get("/")
async def read_auth():
    return {"auth": "auth"}
