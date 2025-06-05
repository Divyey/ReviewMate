from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.crud import create_pull_request, get_pull_requests

router = APIRouter(prefix="/prs", tags=["pull_requests"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_pr(title: str, description: str, db: Session = Depends(get_db)):
    return create_pull_request(db, title, description)

@router.get("/")
def list_prs(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_pull_requests(db, skip, limit)
