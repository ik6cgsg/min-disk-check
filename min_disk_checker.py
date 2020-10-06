from circle import *
from point import *


class MinDiskCheckerException(Exception):
    pass


class MinDiskChecker(object):
    def __init__(self):
        self.coords: [int] = []
        self.points: [Point] = []

    def _all_points_inside(self) -> bool:
        edge_points = [self.points[i] for i in self.coords]
        disk = Circle.create_from_points(edge_points)
        print("MINDISK: ", disk)
        for p in self.points:
            if (p.y - disk.y) ** 2 + (p.x - disk.x) ** 2 > disk.r ** 2:
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
        # TODO: if len(coords) == 3:
        return False
