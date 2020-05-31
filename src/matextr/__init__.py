"""
    Matrix extracting package
"""

from aiohttp import ClientSession

from .transform import transform_raw_data


async def get_matrix(url: str):
    async with ClientSession() as session:
        async with session.get(url) as resp:
            raw_data = await resp.text()
            result = transform_raw_data(raw_data)
    return result
