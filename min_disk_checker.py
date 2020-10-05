from point import *


class MinDiskChecker(object):
    @staticmethod
    def is_disk_minimal(coords: [int], points: [Point]) -> bool:
        if len(coords) == 0:
            return False
        if len(coords) == 1:
            if len(points) == 1:
                return True
            else:
                return False
        # TODO: check all points inside
        if len(coords) == 2:
            return True
        # TODO: if len(coords) == 3:
        return False
