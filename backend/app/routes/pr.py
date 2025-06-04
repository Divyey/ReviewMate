from fastapi import APIRouter, Query
import requests

router = APIRouter()

@router.get("/fetch-pr")
def fetch_pr(owner: str = Query(...), repo: str = Query(...), pr_number: int = Query(...)):
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}"
    headers = {"Accept": "application/vnd.github+json"}
    response = requests.get(url, headers=headers)
    return response.json()
