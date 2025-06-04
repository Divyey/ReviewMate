from fastapi import APIRouter, Query, Depends
import requests
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import PullRequest

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/fetch-pr")
def fetch_pr(
    owner: str = Query(...), 
    repo: str = Query(...), 
    pr_number: int = Query(...),
    db: Session = Depends(get_db)
):
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}"
    headers = {"Accept": "application/vnd.github+json"}
    response = requests.get(url, headers=headers)
    pr_json = response.json()
    # Store in DB
    pr = PullRequest(
        owner=owner,
        repo=repo,
        pr_number=pr_number,
        pr_data=pr_json
    )
    db.add(pr)
    db.commit()
    db.refresh(pr)
    return pr_json
