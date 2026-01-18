from fastapi import FastAPI
from dotenv import load_dotenv
from app.database import engine, Base, get_db, wait_for_db
from contextlib import asynccontextmanager

from fastapi import Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.user import User


# Load environment variables from .env file
load_dotenv(".env.example")

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    wait_for_db(max_retries=10, delay=3)
    yield
    # Shutdown (optional cleanup)
    print("👋 Application shutdown")

app = FastAPI(
    title="AI Travel Planner API",
    lifespan=lifespan
)

@app.get("/health")
def health_check():
    return {"status": "OK"}

@app.get("/")
def root():
    return {"message": "Welcome to AI_travel_planner API"}

@app.post("/users")
def create_user(email: str, password: str, db: Session = Depends(get_db)):
    user = User(email=email, password_hash=password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"id": user.id, "email": user.email}