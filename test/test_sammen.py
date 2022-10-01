import pytest

from sammen.sammen import main


@pytest.mark.asyncio
async def test_main():
    result = await main(['foo'])
    assert result == 2
