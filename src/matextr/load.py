"""
    Load module
"""


def load_data(matrix):
    mln = len(matrix)
    coords = Сoordinates(mln)
    result = []
    for _ in range(mln ** 2):
        x, y = coords.next()
        result.append(matrix[x][y])
    return result


class Сoordinates:
    def __init__(self, sqlnght: int):
        self.square_length = sqlnght
        self.offsets = ((1, 0), (0, 1), (-1, 0), (0, -1))
        self.visited = []
        self.x = None
        self.y = None
        self.next_offset = 0

    def next(self):
        if self.x is None and self.y is None:
            self.x, self.y = self._init()
        else:
            next_x, next_y = self._bias()
            if self._lost_course(next_x, next_y):
                self._turn_left()
                next_x, next_y = self._bias()
            self.x, self.y = next_x, next_y
        self.visited.append((self.x, self.y))
        return (self.x, self.y)

    def _init(self):
        self.x, self.y = 0, 0
        return (self.x, self.y)

    def _bias(self):
        inc = self.offsets[self.next_offset]
        next_x = self.x + inc[0]
        next_y = self.y + inc[1]
        return next_x, next_y

    def _lost_course(self, cx: int, cy: int):
        return cx >= self.square_length or cx < 0 or \
            cy >= self.square_length or cy < 0 or \
            (cx, cy) in self.visited

    def _turn_left(self):
        self.next_offset += 1
        if self.next_offset >= len(self.offsets):
            self.next_offset = 0