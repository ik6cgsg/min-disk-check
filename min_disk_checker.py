import numpy
from point import *


class MinDiskCheckerException(Exception):
    pass


def det3x3(a) -> int:
    return a[0][0] * (a[1][1] * a[2][2] - a[2][1] * a[1][2]) - \
           a[1][0] * (a[0][1] * a[2][2] - a[2][1] * a[0][2]) + \
           a[2][0] * (a[0][1] * a[1][2] - a[1][1] * a[0][2])


def det4x4(a) -> int:
    return a[0][0] * det3x3([
        [a[1][1], a[1][2], a[1][3]],
        [a[2][1], a[2][2], a[2][3]],
        [a[3][1], a[3][2], a[3][3]]
    ]) - a[0][1] * det3x3([
        [a[1][0], a[1][2], a[1][3]],
        [a[2][0], a[2][2], a[2][3]],
        [a[3][0], a[3][2], a[3][3]]
    ]) + a[0][2] * det3x3([
        [a[1][0], a[1][1], a[1][3]],
        [a[2][0], a[2][1], a[2][3]],
        [a[3][0], a[3][1], a[3][3]]
    ]) - a[0][3] * det3x3([
        [a[1][0], a[1][1], a[1][2]],
        [a[2][0], a[2][1], a[2][2]],
        [a[3][0], a[3][1], a[3][2]]
    ])


class MinDiskChecker(object):
    def __init__(self):
        self.coords: [int] = []
        self.points: [Point] = []
        self.edge_points: [Point] = []
        self.sign = None

    def _inside_for_2_points(self, p: Point) -> bool:
        p0 = self.edge_points[0]
        p1 = self.edge_points[1]
        return (p.x - p0.x) * (p.x - p1.x) + (p.y - p0.y) * (p.y - p1.y) <= 0

    # Check middle point of p0p1 side
    def _get_sign_for_3_points(self, p0: Point, p1: Point, p2: Point):
        p = p1 + p0  # doubled middle of p0p1 side
        matrix = [
            [p.x ** 2 + p.y ** 2, p.x, p.y, 2],
            [4 * p0.x ** 2 + 4 * p0.y ** 2, 2 * p0.x, 2 * p0.y, 2],
            [4 * p1.x ** 2 + 4 * p1.y ** 2, 2 * p1.x, 2 * p1.y, 2],
            [4 * p2.x ** 2 + 4 * p2.y ** 2, 2 * p2.x, 2 * p2.y, 2],
        ]  # doubled matrix respectively
        if det4x4(matrix) < 0:
            self.sign = 1
        else:
            self.sign = -1

    def _inside_for_3_points(self, p: Point) -> bool:
        p0 = self.edge_points[0]
        p1 = self.edge_points[1]
        p2 = self.edge_points[2]
        matrix = [
            [p.x ** 2 + p.y ** 2, p.x, p.y, 1],
            [p0.x ** 2 + p0.y ** 2, p0.x, p0.y, 1],
            [p1.x ** 2 + p1.y ** 2, p1.x, p1.y, 1],
            [p2.x ** 2 + p2.y ** 2, p2.x, p2.y, 1],
        ]
        return self.sign * det4x4(matrix) <= 0

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
        inside = None
        if len(self.coords) == 2:
            inside = self._inside_for_2_points
        elif len(self.coords) == 3:
            inside = self._inside_for_3_points
            self._get_sign_for_3_points(self.edge_points[0], self.edge_points[1], self.edge_points[2])
        else:
            return False
        for p in self.points:
            if not inside(p):
                return False
        return True

    def is_disk_minimal(self, coords: [int], points: [Point]) -> bool:
        self.sign = None
        if len(coords) > len(points):
            raise MinDiskCheckerException("Number of indices is larger then number of points")
        if len(coords) > 3:
            raise MinDiskCheckerException("Too many indices")
        if len(coords) == 0:
            if len(points) == 0:
                return True
            else:
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
