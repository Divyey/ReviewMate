from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float, Text
from sqlalchemy.orm import relationship
from .database import Base
from datetime import datetime

class Repository(Base):
    __tablename__ = "repositories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    url = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    pull_requests = relationship("PullRequest", back_populates="repository")

class PullRequest(Base):
    __tablename__ = "pull_requests"
    id = Column(Integer, primary_key=True, index=True)
    repo_id = Column(Integer, ForeignKey("repositories.id"), nullable=False)
    branch = Column(String, nullable=False)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    status = Column(String, default="open")
    score = Column(Float, nullable=True)
    last_reviewed = Column(DateTime, nullable=True)
    most_common_issue = Column(String, nullable=True)
    ai_suggestions = Column(Text, nullable=True)
    warnings_count = Column(Integer, default=0)
    errors_count = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    repository = relationship("Repository", back_populates="pull_requests")
    issues = relationship("Issue", back_populates="pull_request", cascade="all, delete-orphan")

class Issue(Base):
    __tablename__ = "issues"
    id = Column(Integer, primary_key=True, index=True)
    pr_id = Column(Integer, ForeignKey("pull_requests.id"), nullable=False)
    file_path = Column(String, nullable=False)
    issue_type = Column(String, nullable=False)  # warning/error
    severity = Column(String, nullable=True)     # low/medium/high
    description = Column(Text, nullable=False)
    line_start = Column(Integer, nullable=True)
    line_end = Column(Integer, nullable=True)
    suggestion = Column(Text, nullable=True)
    explanation = Column(Text, nullable=True)
    feedback = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    pull_request = relationship("PullRequest", back_populates="issues")
