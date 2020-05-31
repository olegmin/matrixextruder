# Necessary libraries
import asyncio
from matextr import get_matrix


# Script configuration
URL = 'https://f003.backblazeb2.com/file/am-avito/matrix.txt'


# Launch the script
if __name__ == "__main__":
    r = asyncio.run(get_matrix(URL))
    print(r)
