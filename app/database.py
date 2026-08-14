from sqlalchemy import create_engine , URL
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv
from app.config import settings



engine = create_engine(
   settings.DATABASE_URL,
    echo=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()
