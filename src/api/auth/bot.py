from fastapi import APIRouter

router = APIRouter("/bot")

@router.post("/login")
async def auth_login_bot():
    return {'data': 'Success'}