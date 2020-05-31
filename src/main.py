import asyncio
from aiohttp import ClientSession

from matextr.transform import transform_raw_data

URL = 'https://f003.backblazeb2.com/file/am-avito/matrix.txt'


async def get_matrix(url: str):
    async with ClientSession() as session:
        async with session.get(url) as resp:
            raw_data = await resp.text()
            result = transform_raw_data(raw_data)
    return result


if __name__ == "__main__":
    r = asyncio.run(get_matrix(URL))
    print(r)
