"""
    Matrix extracting package
"""
from .extract import extract_data
from .transform import transform_raw_data
from .load import load_data


async def get_matrix(url: str):
    response = await extract_data(url)
    print(f"Extracted raw data:\n{response}")
    matrix = transform_raw_data(response)
    print(f"Transformed matrix:\n{matrix}\n")
    result = load_data(matrix)
    return result
