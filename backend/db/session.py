from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import settings
from typing import Any, Generator

SQLALCHEMY_DB_URL = settings.DATABASE_URL
engine = create_engine(SQLALCHEMY_DB_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def get_db() -> Generator:
	try:
		db = SessionLocal()
		yield db
	finally:
		db.close()
		