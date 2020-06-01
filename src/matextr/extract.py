"""
    Extract module
"""
from aiohttp import ClientSession


async def extract_data(url: str):
    async with ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.text()
