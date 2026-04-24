from fastapi import APIRouter, HTTPException, status, Depends
from src.models import Schedule
from src.dependencies import get_db
from src.schemas import ScheduleSchema
from sqlalchemy.orm import Session

router = APIRouter(prefix="/schedule", tags=["schedule"])


@router.post("/")
async def create_schedule(schedule_data: ScheduleSchema, session: Session = Depends(get_db)):
    new_schedule = Schedule(
        **schedule_data.model_dump()
    )
    session.add(new_schedule)
    session.commit()
    return HTTPException(status_code=status.HTTP_201_CREATED, detail="Schedule created")
