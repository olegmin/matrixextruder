"""
    Load module
"""


def load_data(matrix, flag=True, result=[]):
    if len(matrix) <= 0:
        return result
    else:
        print(f"Inserted matrix: {matrix}")
        if flag:
            transposed_matrix = list(zip(*matrix))
            print(f"transposed matrix: {transposed_matrix}")
            for item in transposed_matrix.pop(0):
                result.append(item)
        else:
            transposed_matrix = list(zip(*matrix[::-1]))
            print(f"transposed matrix: {transposed_matrix}")
            dev = len(transposed_matrix) - 1
            for item in transposed_matrix.pop(dev)[::-1]:
                result.append(item)
        print(f"matrix after pop: {transposed_matrix}\n")
        return load_data(transposed_matrix, flag!=True)
