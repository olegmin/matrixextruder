import asyncio
from aiohttp import ClientSession


URL = 'https://f003.backblazeb2.com/file/am-avito/matrix.txt'


async def get_matrix(url: str):
    async with ClientSession() as session:
        async with session.get(url) as resp:
            # TODO: resolve problem with server (responses not 2XX)
            result = await resp.text()
    return result


if __name__ == "__main__":
    r = asyncio.run(get_matrix(URL))
    print(r)
