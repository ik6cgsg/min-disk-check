import unittest
from min_disk_checker import *
from point import *
import warnings


class TestMinDiskChecker(unittest.TestCase):
    def setUp(self) -> None:
        self.mdc = MinDiskChecker()
        warnings.filterwarnings("error")

    def test_min_disk_0_points(self):
        points = []
        coords = []
        self.assertEqual(self.mdc.is_disk_minimal(coords, points), True)

    def test_min_disk_0_coords(self):
        points = [
            Point(100, 100),
            Point(100, 200)
        ]
        coords = []
        self.assertEqual(self.mdc.is_disk_minimal(coords, points), False)

    def test_min_disk_1_point_ok(self):
        points = [
            Point(100, 100)
        ]
        coords = [0]
        self.assertEqual(self.mdc.is_disk_minimal(coords, points), True)

    def test_min_disk_1_point_bad(self):
        points = [
            Point(100, 100),
            Point(100, 50)
        ]
        coords = [0]
        self.assertEqual(self.mdc.is_disk_minimal(coords, points), False)

    def test_min_disk_2_points_ok(self):
        points = [
            Point(100, 100),
            Point(100, 0),
            Point(100, 50),
            Point(120, 40),
            Point(90, 60),
            Point(149, 50)
        ]
        coords = [0, 1]
        self.assertEqual(self.mdc.is_disk_minimal(coords, points), True)

    def test_min_disk_2_points_ok_2(self):
        points = [
            Point(100, 100),
            Point(100, 0),
            Point(100, 50),
            Point(120, 40),
            Point(90, 60),
            Point(149, 50)
        ]
        coords = [1, 0]
        self.assertEqual(self.mdc.is_disk_minimal(coords, points), True)

    def test_min_disk_2_points_wrong(self):
        points = [
            Point(100, 100)
        ]
        coords = [0, 1]
        with self.assertRaises(MinDiskCheckerException):
            self.mdc.is_disk_minimal(coords, points)

    def test_min_disk_2_points_bad(self):
        points = [
            Point(100, 100),
            Point(100, 0),
            Point(100, 50),
            Point(120, 40),
            Point(90, 60),
            Point(149, 50),
            Point(200, 200)
        ]
        coords = [0, 1]
        self.assertEqual(self.mdc.is_disk_minimal(coords, points), False)

    def test_min_disk_2_points_bad_2(self):
        points = [
            Point(100, 100),
            Point(100, 0),
            Point(100, 50),
            Point(120, 40),
            Point(90, 60),
            Point(149, 50),
            Point(200, 200)
        ]
        coords = [1, 0]
        self.assertEqual(self.mdc.is_disk_minimal(coords, points), False)

    def test_min_disk_3_points_ok(self):
        points = [
            Point(0, 30),
            Point(24, -18),
            Point(-18, -24),
            Point(18, 24),
            Point(0, 0),
            Point(10, 15),
            Point(-24, 18),
            Point(-6, 21),
            Point(11, -16),
            Point(15, -25),
        ]
        coords = [0, 1, 2]
        self.assertEqual(self.mdc.is_disk_minimal(coords, points), True)

    def test_min_disk_3_points_ok_2(self):
        points = [
            Point(6, 3),
            Point(1, -2),
            Point(-3, 6),
            Point(0, 0),
            Point(2, 4),
            Point(4, 7)
        ]
        coords = [2, 1, 0]
        self.assertEqual(self.mdc.is_disk_minimal(coords, points), True)

    def test_min_disk_3_points_ok_3(self):
        points = [
            Point(6, 3),
            Point(1, -2),
            Point(-3, 6),
            Point(0, 0),
            Point(2, 4),
            Point(4, 7)
        ]
        coords = [1, 0, 2]
        self.assertEqual(self.mdc.is_disk_minimal(coords, points), True)

    def test_min_disk_3_points_bad_obtuse(self):
        points = [
            Point(6, 3),
            Point(1, -2),
            Point(0, 0),
            Point(2, 4),
            Point(4, 7),
        ]
        coords = [0, 1, 4]
        self.assertEqual(self.mdc.is_disk_minimal(coords, points), False)

    def test_min_disk_3_points_ok_large_num(self):
        points = [
            Point(948904, 106447),
            Point(344710, 448131),
            Point(803743, 922708),
            Point(78651, 108263)
        ]
        coords = [2, 3, 0]
        self.assertEqual(self.mdc.is_disk_minimal(coords, points), True)

    def test_min_disk_3_points_ok_large_num_2(self):
        points = [
            Point(948904, 106447),
            Point(344710, 448131),
            Point(803743, 922708),
            Point(78651, 108263)
        ]
        coords = [3, 0, 2]
        self.assertEqual(self.mdc.is_disk_minimal(coords, points), True)

    def test_min_disk_3_points_ok_large_num_3(self):
        points = [
            Point(948904, 106447),
            Point(344710, 448131),
            Point(803743, 922708),
            Point(78651, 108263)
        ]
        coords = [0, 3, 2]
        self.assertEqual(self.mdc.is_disk_minimal(coords, points), True)

    def test_min_disk_3_points_ok_extra_large_num(self):
        points = [
            Point(9489040000, 1064470000),
            Point(3447100000, 4481310000),
            Point(8037430000, 9227080000),
            Point(786510000, 1082630000)
        ]
        coords = [2, 0, 3]
        self.assertEqual(self.mdc.is_disk_minimal(coords, points), True)