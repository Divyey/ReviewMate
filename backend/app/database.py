from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

# Load environment variables from .env file (recommended for security)
load_dotenv()

# Use environment variable, fallback to a default if not set
SQLALCHEMY_DATABASE_URL = os.getenv(
    'DATABASE_URL',
    'postgresql://reviewmate_user:Divyey123@localhost/reviewmate_dev'
)
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
