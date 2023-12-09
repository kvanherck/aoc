#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

if len(sys.argv) == 1:
    gridsize = 4000000
else:
    gridsize = 20

sensors = []
points = set()

for fields in inputRE(r'Sensor at x=(\d+), y=(\d+): closest beacon is at x=(-?\d+), y=(-?\d+)'):
    sx, sy, bx, by = map(int, fields)
    d = abs(sx - bx) + abs(sy - by)
    sensors.append((sx, sy, d))

def addIntersection(x1, y1, d1, x2, y2, d2):
    # Intersection of
    #   y - y1 = x - x1 + d1
    #   y - y2 = -(x - x2 + d2)
    # is
    #   x = ((x1 + x2) + (y2 - y1) - (d1 + d2)) / 2
    #   y = ((x2 - x1) + (y1 + y2) + (d1 - d2)) / 2
    x = ((x1 + x2) + (y2 - y1) - (d1 + d2)) // 2
    y = ((y1 + y2) + (x2 - x1) + (d1 - d2)) // 2
    if x < 0 or x > gridsize:
        return
    if y < 0 or y > gridsize:
        return
    points.add((x, y))

print(f'Processing {len(sensors)} sensors')
for i in range(len(sensors)):
    for j in range(len(sensors)):
        if i == j:
            continue
        x1, y1, d1 = sensors[i]
        d1 += 1
        x2, y2, d2 = sensors[j]
        d2 += 1
        # Calculate 4 intersections for positive & negative distances
        # using positive slope for sensor 1 and negative slope for sensor 2.
        # The other slopes are handled by swapping sensor 1 and 2.
        addIntersection(x1, y1, d1, x2, y2, d2)
        addIntersection(x1, y1, d1, x2, y2, -d2)
        addIntersection(x1, y1, -d1, x2, y2, d2)
        addIntersection(x1, y1, -d1, x2, y2, -d2)

print(f'Found {len(points)} candidate points')

def isInRange(sx, sy, d, x, y):
    return abs(sx - x) + abs(sy - y) <= d

matches = []
for (x, y) in points:
    if any(isInRange(sx, sy, d, x, y) for sx, sy, d in sensors):
        continue
    print(f'({x}, {y})')
    matches.append((x, y))

assert(len(matches) == 1)
x, y = matches[0]
print(x * 4000000 + y)
