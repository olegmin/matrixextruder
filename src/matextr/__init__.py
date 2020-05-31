"""
    Matrix extracting package
"""
from .extract import extract_data
from .transform import transform_raw_data
from .load import load_data


async def get_matrix(url: str):
    response = await extract_data(url)
    print(f"Extracted raw data:\n{response}\n\n")
    matrix = transform_raw_data(response)
    result = load_data(matrix)
    return result
