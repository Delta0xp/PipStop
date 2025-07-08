from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/api/auth", tags=["auth"])

class User(BaseModel):
    email: str
    password: str

@router.post("/signup")
async def signup(user: User):
    # You can add DB logic here later
    return {"message": f"User {user.email} signed up successfully!"}

@router.post("/login")
async def login(user: User):
    # You can add auth logic here later
    return {"message": f"User {user.email} logged in successfully!"}
