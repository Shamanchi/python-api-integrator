from fastapi import APIRouter
from app.services.client import APIClient

router = APIRouter()

@router.get('/health')
async def health():
    return {'status': 'ok'}

@router.get('/users')
async def get_users():
    async with APIClient() as client:
        return await client.get('/users')