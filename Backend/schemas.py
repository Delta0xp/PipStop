from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    email: str
    password: str
    role: Optional[str] = "member"

class UserOut(BaseModel):
    id: int
    email: str
    role: str  

    class Config:
        from_attributes = True  

class Token(BaseModel):
    access_token: str
    token_type: str
