from fastapi import APIRouter

router = APIRouter(prefix="/api/members", tags=["members"])

@router.get("/")
async def get_members():
    return [
        {"name": "Alex", "role": "Data Engineer"},
        {"name": "Sam", "role": "AI Researcher"},
    ]
