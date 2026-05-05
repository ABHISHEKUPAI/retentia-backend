from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.crud import syllabus as syllabus_crud
from app.schemas.syllabus import SubjectOut

router = APIRouter(prefix="/syllabus", tags=["Syllabus"])


@router.get("/", response_model=List[SubjectOut])
def get_syllabus(db: Session = Depends(get_db)):
    return syllabus_crud.get_syllabus(db)
