from fastapi import FastAPI
from app.routes import pr_routes

app = FastAPI()
app.include_router(pr_routes.router)
