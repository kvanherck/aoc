#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

if len(sys.argv) == 1:
    targety = 2000000
else:
    targety = 10

nobeacons = set()
beacons = set()

for fields in inputRE(r'Sensor at x=(\d+), y=(\d+): closest beacon is at x=(\d+), y=(\d+)'):
    sx, sy, bx, by = map(int, fields)
    if by == targety:
        beacons.add(bx)
    d = abs(sx - bx) + abs(sy - by)
    n = d - abs(targety - sy)
    if n > 0:
        m = 2 * d + 1 - 2 * abs(targety - sy)
        for x in range(sx - n, sx + n + 1):
            nobeacons.add(x)

print(len(nobeacons) - len(beacons))
