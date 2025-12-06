from fastapi import APIRouter

router = APIRouter("/web")

@router.post("/login")
async def auth_web():
    return {'data': 'Success'}