import httpx
from tenacity import retry, stop_after_attempt, wait_exponential
from loguru import logger
from app.core.config import settings


class APIClient:
    def __init__(self):
        self.base_url = settings.api_base_url
        self.api_key = settings.api_key
        self.timeout = settings.api_timeout
        self.client = httpx.AsyncClient(
            base_url=self.base_url,
            timeout=self.timeout,
            headers={'Authorization': f'Bearer {self.api_key}'} if self.api_key else {}
        )
    
    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1.5, min=1, max=10)
    )
    async def get(self, path: str, params: dict = None):
        response = await self.client.get(path, params=params)
        response.raise_for_status()
        return response.json()
    
    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1.5, min=1, max=10)
    )
    async def post(self, path: str, data: dict):
        response = await self.client.post(path, json=data)
        response.raise_for_status()
        return response.json()
    
    async def close(self):
        await self.client.aclose()