import asyncio
from matextr import get_matrix


URL = 'https://f003.backblazeb2.com/file/am-avito/matrix.txt'


if __name__ == "__main__":
    r = asyncio.run(get_matrix(URL))
    print(r)
