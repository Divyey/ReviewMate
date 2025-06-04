from fastapi import FastAPI
from app.routes import pr

app = FastAPI()
app.include_router(pr.router)
