"""
    Load module
"""


def load_data(matrix, flat=[]):
    if len(matrix) <= 0:
        return flat
    else:
        transposed_matrix = list(zip(*matrix))
        for item in transposed_matrix.pop(0):
            flat.append(item)
        return load_data(transposed_matrix)
