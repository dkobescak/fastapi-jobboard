from sqlalchemy import Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship, Mapped, mapped_column
from typing import List, Optional, Annotated
from datetime import datetime


class Base(DeclarativeBase):
	pass


class Job(Base):
	__tablename__ = "jobs"
	
	id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
	title: Mapped[str] = mapped_column(String, nullable=False)
	company: Mapped[str] = mapped_column(String, nullable=False)
	company_url: Mapped[Optional[str]]
	location: Mapped[str] = mapped_column(String, nullable=False)
	description: Mapped[Optional[str]]
	date_posted: Mapped[Optional[datetime]]
	is_active: Mapped[bool] = mapped_column(Boolean, default=True)
	owner_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'))
	owner: Mapped["User"] = relationship("User", back_populates="jobs")
	
	
class User(Base):
	__tablename__ = "users"
	
	id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
	username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
	email: Mapped[str] = mapped_column(String, nullable=False, unique=True, index=True)
	hashed_password: Mapped[str] = mapped_column(String, nullable=False)
	is_active: Mapped[bool] = mapped_column(Boolean, default=True)
	is_superuser: Mapped[bool] = mapped_column(Boolean, default=False)
	jobs: Mapped["Job"] = relationship("Job", back_populates="owner")
