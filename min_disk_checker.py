import numpy
from point import *


class MinDiskCheckerException(Exception):
    pass


def det(A):
    n, _ = numpy.shape(A)
    if n == 1:
        return A[0, 0]
    else:
        s = 0
        for i in range(n):
            l = [x for x in range(n) if x != i]
            s += (-1) ** i * A[0, i] * det(A[1:, l])
        return s


class MinDiskChecker(object):
    def __init__(self):
        self.coords: [int] = []
        self.points: [Point] = []
        self.edge_points: [Point] = []

    def _inside_for_2_points(self, p: Point) -> bool:
        p0 = self.edge_points[0]
        p1 = self.edge_points[1]
        return (p.x - p0.x) * (p.x - p1.x) + (p.y - p0.y) * (p.y - p1.y) <= 0

    def _inside_for_3_points(self, p: Point) -> bool:
        p0 = self.edge_points[0]
        p1 = self.edge_points[1]
        p2 = self.edge_points[2]
        matrix = numpy.array([
            [p.x ** 2 + p.y ** 2, p.x, p.y, 1],
            [p0.x ** 2 + p0.y ** 2, p0.x, p0.y, 1],
            [p1.x ** 2 + p1.y ** 2, p1.x, p1.y, 1],
            [p2.x ** 2 + p2.y ** 2, p2.x, p2.y, 1],
        ], dtype=int)
        return det(matrix) >= 0

    def _inside(self, p: Point) -> bool:
        if len(self.coords) == 2:
            return self._inside_for_2_points(p)
        if len(self.coords) == 3:
            return self._inside_for_3_points(p)
        return False

    def _is_obtuse_triangle(self) -> bool:
        p0 = self.edge_points[0]
        p1 = self.edge_points[1]
        p2 = self.edge_points[2]
        side0sqr = (p0.x - p1.x) ** 2 + (p0.y - p1.y) ** 2
        side1sqr = (p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2
        side2sqr = (p2.x - p0.x) ** 2 + (p2.y - p0.y) ** 2
        if (side0sqr + side1sqr > side2sqr) and (side1sqr + side2sqr > side0sqr) and (side2sqr + side0sqr > side1sqr):
            return True
        return False

    def _all_points_inside(self) -> bool:
        self.edge_points = [self.points[i] for i in self.coords]
        for p in self.points:
            if not self._inside(p):
                return False
        return True

    def is_disk_minimal(self, coords: [int], points: [Point]) -> bool:
        if len(coords) > len(points):
            raise MinDiskCheckerException("Number of indices is larger then number of points")
        if len(coords) > 3:
            raise MinDiskCheckerException("Too many indices")
        if len(coords) == 0:
            return False
        if len(coords) == 1:
            if len(points) == 1:
                return True
            else:
                return False
        self.coords = coords
        self.points = points
        if not self._all_points_inside():
            return False
        if len(coords) == 2:
            return True
        if len(coords) == 3 and self._is_obtuse_triangle():
            return True
        return False
