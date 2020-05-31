"""
    Transform module
"""


def transform_raw_data(s: str):
    matrix = []
    print(s)
    for line in s.split('\n'):
        if line.startswith('+'):
            continue
        line_list = []
        for subline in line.split('|'):
            item = subline.strip()
            if item.isdigit():
                line_list.append(int(item))
        if len(line_list) > 0:
            matrix.append(line_list)
    return matrix
