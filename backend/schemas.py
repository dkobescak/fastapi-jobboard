from typing import Optional
from pydantic import BaseModel, EmailStr


# used for data validation of new users
class UserCreate(BaseModel):
	username: str
	email: EmailStr
	password: str
	
