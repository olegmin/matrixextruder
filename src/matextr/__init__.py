"""
    Matrix extracting package
"""
from aiohttp import ClientSession

from .transform import transform_raw_data
from .load import load_data


async def get_matrix(url: str):
    async with ClientSession() as session:
        async with session.get(url) as resp:
            response = await resp.text()
            matrix = transform_raw_data(response)
            result = load_data(matrix)
    return result
