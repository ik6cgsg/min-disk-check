import sys

from min_disk_checker import *
from point import *
import time

if __name__ == '__main__':
    start = time.time()

    if len(sys.argv) != 2:
        print("Usage: /path/to/python3.x main.py <data_file>\n"
              "data_file format:\n"
              "\tFirst line - '[int] [int] [int]\\n' - indices of disk edge points from list below\n"
              "\tFurther - '<int> <int>\\n' - 2d points coordinates")
        exit()
    try:
        file = open(sys.argv[1])
        coordStr = file.readline()
        coords = [int(x) for x in coordStr.split()]
        points = []
        for line in file:
            point = Point.create_from_str(line)
            points.append(point)
        print("POINTS LEN:", len(points))
        file.close()
        mdc = MinDiskChecker()
        print("Is disk minimal? ", mdc.is_disk_minimal(coords, points))
    except IOError:
        print("ERROR: File not accessible")
    except ValueError:
        print("ERROR: Data must be integer")
    except PointException as pe:
        print("Point ERROR: " + str(pe))
    except MinDiskCheckerException as me:
        print("MinDiskChecker ERROR: " + str(me))

    end = time.time()
    print("TIME:", end - start)
