class PointException(Exception):
    pass


class Point(object):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    @staticmethod
    def create_from_str(string: str):
        if not string:
            raise PointException("Wrong string format")
        try:
            coords = [int(x) for x in string.split()]
            if len(coords) != 2:
                raise PointException("Wrong number of coordinates")
            return Point(coords[0], coords[1])
        except ValueError:
            raise PointException("Coordinates are not int")

    def len(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, num: int):
        return Point(self.x * num, self.y * num)

    def __str__(self):
        return "Point(%s, %s)" % (self.x, self.y)

    def __repr__(self):
        return self.__str__()
