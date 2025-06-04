from sqlalchemy import Column, Integer, String, JSON
from app.database import Base

class PullRequest(Base):
    __tablename__ = "pull_requests"

    id = Column(Integer, primary_key=True, index=True)
    owner = Column(String, index=True)
    repo = Column(String, index=True)
    pr_number = Column(Integer, index=True)
    pr_data = Column(JSON)
