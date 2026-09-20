import pytest
from unittest.mock import AsyncMock, MagicMock, patch


@pytest.mark.asyncio
async def test_health():
    from app.api.routes import health
    result = await health()
    assert result == {'status': 'ok'}


@pytest.mark.asyncio
async def test_config():
    from app.core.config import settings
    assert settings.log_level == 'INFO'