#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *
import numpy as np

cubes = []
for fields in inputRE(r'(on|off) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)'):
    state = int(fields[0] == 'on')
    fields = map(int, fields[1:])
    x1, x2, y1, y2, z1, z2 = fields
    assert x1 <= x2
    assert y1 <= y2
    assert z1 <= z2
    cubes.append((state, x1, x2, y1, y2, z1, z2))

def intersection(c1, c2):
    c1state, c1x1, c1x2, c1y1, c1y2, c1z1, c1z2 = c1
    c2state, c2x1, c2x2, c2y1, c2y2, c2z1, c2z2 = c2
    x1 = max(c1x1, c2x1)
    x2 = min(c1x2, c2x2)
    if x1 > x2:
        return None
    y1 = max(c1y1, c2y1)
    y2 = min(c1y2, c2y2)
    if y1 > y2:
        return None
    z1 = max(c1z1, c2z1)
    z2 = min(c1z2, c2z2)
    if z1 > z2:
        return None
    return c1state, x1, x2, y1, y2, z1, z2

def intersections(c1, cubes):
    intersections = []
    for c in cubes:
        i = intersection(c1, c)
        if i is not None:
            intersections.append(i)
    return intersections

def volume(c):
    state, x1, x2, y1, y2, z1, z2 = c
    n = (x2 - x1 + 1) * (y2 - y1 + 1) * (z2 - z1 + 1)
    return n

def sum_all(cubes):
    if len(cubes) == 0:
        return 0
    c = cubes[0]
    remaining = cubes[1:]
    v = volume(c)
    v += sum_all(remaining)
    v -= sum_all(intersections(c, remaining))
    return v

def sum_on(cubes):
    if len(cubes) == 0:
        return 0
    c = cubes[0]
    remaining = cubes[1:]
    state, x1, x2, y1, y2, z1, z2 = c
    if state == 0:
        return sum_on(remaining)
    else:
        v = volume(c)
        v += sum_on(remaining)
        v -= sum_all(intersections(c, remaining))
        return v

start = timer()
print(len(cubes))
print(sum_on(cubes))
print(f'Finished in {timer() - start:.03}s')
