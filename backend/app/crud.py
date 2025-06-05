from sqlalchemy.orm import Session
from .models import PullRequest

def create_pull_request(db: Session, title: str, description: str):
    pr = PullRequest(title=title, description=description)
    db.add(pr)
    db.commit()
    db.refresh(pr)
    return pr

def get_pull_requests(db: Session, skip: int = 0, limit: int = 10):
    return db.query(PullRequest).offset(skip).limit(limit).all()
