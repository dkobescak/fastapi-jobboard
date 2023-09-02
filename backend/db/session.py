from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, as_declarative, declared_attr
from core.config import settings
from typing import Any

SQLALCHEMY_DB_URL = settings.DATABASE_URL
engine = create_engine(SQLALCHEMY_DB_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()  # why not just this?


# @as_declarative()
# class Base:cd
# 	id: Any
# 	__name__: str
#
# 	def __tablename__(cls) -> str:
# 		return cls.__name__.lower()
	
	