from .. import utils
from fastapi import APIRouter, Depends

router = APIRouter(prefix="/api/members", tags=["members"])

@router.get("/", dependencies=[Depends(utils.get_current_user)])
async def get_members():
    return [
        {"name": "Alex", "role": "Data Engineer"},
        {"name": "Sam", "role": "AI Researcher"},
    ]
