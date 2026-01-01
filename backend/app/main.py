from fastapi import FastAPI
from dotenv import load_dotenv
from app.database import engine, Base, get_db, wait_for_db
from contextlib import asynccontextmanager

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
