from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

from sqlalchemy.exc import OperationalError
import time

# Load environment variables from .env file
load_dotenv(".env.example")
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

def wait_for_db(max_retries=10, delay=3):
    retries = 0
    while retries < max_retries:
        try:
            with engine.connect():
                print("✅ Database is ready!")
                return
        except OperationalError:
            retries += 1
            print(f"⏳ Waiting for DB... ({retries}/{max_retries})")
            time.sleep(delay)

    raise Exception("❌ Database not ready after multiple retries")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

