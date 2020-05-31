"""
    Matrix extracting package
"""
from aiohttp import ClientSession

from .transform import transform_raw_data


async def get_matrix(url: str):
    async with ClientSession() as session:
        async with session.get(url) as resp:
            response = await resp.text()
            result = transform_raw_data(response)
    return result
