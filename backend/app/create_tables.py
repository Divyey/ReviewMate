from app.database import Base, engine
from app.models import PullRequest

Base.metadata.create_all(bind=engine)
print("Tables created!")
