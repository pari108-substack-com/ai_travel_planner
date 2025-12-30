from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="AI Travel Planner API")

@app.get("/health")
def health_check():
    return {"status": "OK"}

@app.get("/")
def root():
    return {"message": "Welcome to AI_travel_planner API"}
