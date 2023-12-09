#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *
import numpy as np

def overlaps(c1, c2):
    c1state, c1x1, c1x2, c1y1, c1y2, c1z1, c1z2 = c1
    c2state, c2x1, c2x2, c2y1, c2y2, c2z1, c2z2 = c2
    if c1x2 < c2x1 or c1x1 > c2x2:
        return False
    if c1y2 < c2y1 or c1y1 > c2y2:
        return False
    if c1z2 < c2z1 or c1z1 > c2z2:
        return False
    return True

cubes = []
for fields in inputRE(r'(on|off) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)'):
    state = int(fields[0] == 'on')
    fields = map(int, fields[1:])
    x1, x2, y1, y2, z1, z2 = fields
    assert x1 <= x2
    assert y1 <= y2
    assert z1 <= z2
    cubes.append((state, x1, x2, y1, y2, z1, z2))

def overlapsWithGroup(c, g):
    for cg in g:
        if overlaps(c, cg):
            return True
    return False

remaining = list(range(len(cubes)))
group = []
groups = [group]
while remaining:
    if not group:
        group.append(remaining.pop(0))
    else:
        new = []
        found = False
        for ci in remaining:
            c = cubes[ci]
            gcubes = [cubes[i] for i in group]
            if overlapsWithGroup(c, gcubes):
                group.append(ci)
                found = True
            else:
                new.append(ci)
        remaining = new
        if not found:
            group = []
            groups.append(group)

for i in range(len(groups)):
    g = groups[i]
    g.sort()
    g = [cubes[j] for j in g]
    groups[i] = g

def sum(cubes):
    xbounds = set()
    ybounds = set()
    zbounds = set()

    for state, x1, x2, y1, y2, z1, z2 in cubes:
        xbounds.add(x1 - 0.5)
        xbounds.add(x2 + 0.5)
        ybounds.add(y1 - 0.5)
        ybounds.add(y2 + 0.5)
        zbounds.add(z1 - 0.5)
        zbounds.add(z2 + 0.5)

    xbounds = list(xbounds)
    xbounds.sort()
    ybounds = list(ybounds)
    ybounds.sort()
    zbounds = list(zbounds)
    zbounds.sort()

    print('array size:', len(xbounds) * len(xbounds) * len(xbounds))

    a = np.zeros((len(xbounds)-1, len(ybounds)-1, len(zbounds)-1), dtype=bool)
    for i, c in enumerate(cubes):
        state, x1, x2, y1, y2, z1, z2 = c
        xi1 = xbounds.index(x1 - 0.5)
        xi2 = xbounds.index(x2 + 0.5)
        yi1 = ybounds.index(y1 - 0.5)
        yi2 = ybounds.index(y2 + 0.5)
        zi1 = zbounds.index(z1 - 0.5)
        zi2 = zbounds.index(z2 + 0.5)
        a[xi1:xi2, yi1:yi2, zi1:zi2] = state

    xsizes = []
    for i in range(len(xbounds)-1):
        xsizes.append(round(xbounds[i+1] - xbounds[i]))
    ysizes = []
    for i in range(len(ybounds)-1):
        ysizes.append(round(ybounds[i+1] - ybounds[i]))
    zsizes = []
    for i in range(len(zbounds)-1):
        zsizes.append(round(zbounds[i+1] - zbounds[i]))

    s = 0
    for i in range(len(xbounds)-1):
        aa = np.array(a[i,:,:], dtype=np.int64) * zsizes
        aa = np.sum(aa, axis=1) * ysizes
        s += np.sum(aa) * xsizes[i]
    return s

start = timer()
s = 0
for i, g in enumerate(groups):
    print(f'Processing group {i} of {len(groups)}: {len(g)} cubes')
    s += sum(g)
print(s)
print(f'Finished in {timer() - start:.03}s')
