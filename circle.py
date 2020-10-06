from point import *


class CircleException(Exception):
    pass


class Circle(object):
    def __init__(self, x: float, y: float, r: float):
        self.x = x
        self.y = y
        self.r = r

    @staticmethod
    def create_from_points(points: [Point]):
        if not 1 < len(points) < 4:
            raise CircleException("Too few or too many points")
        if len(points) == 2:
            p0 = points[0]
            p1 = points[1]
            diff = p1 - p0
            diff *= 0.5
            center = p0 + diff
            return Circle(center.x, center.y, diff.len())

    def __str__(self):
        return "Circle(x = %s, y = %s, r = %s)" % (self.x, self.y, self.r)

    def __repr__(self):
        return self.__str__()
