#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *
import numpy as np

tiles = {}
matchingTiles = {}
edge2tile = {}

for chunk in inputChunks():
    header = chunk[0]
    fields = header.split()
    n = int(fields[1][:-1])
    rows = []
    for line in chunk[1:]:
        values = [int(x == '#') for x in line]
        rows.append(values)
    a = np.asarray(rows)
    tiles[n] = a
    matchingTiles[n] = set()
    print(n)
    print(a)
    edges = set()
    edges.add(tuple(a[0,:]))
    edges.add(tuple(a[0,::-1]))
    edges.add(tuple(a[-1,:]))
    edges.add(tuple(a[-1,::-1]))
    edges.add(tuple(a[:,0]))
    edges.add(tuple(a[::-1,0]))
    edges.add(tuple(a[:,-1]))
    edges.add(tuple(a[::-1,-1]))
    for edge in edges:
        if edge not in edge2tile:
            edge2tile[edge] = set()
        edge2tile[edge].add(n)

for edge, tiles in edge2tile.items():
    print(edge, len(tiles), tiles)
    assert len(tiles) in [1, 2], len(tiles)
    if len(tiles) == 2:
        tiles = list(tiles)
        matchingTiles[tiles[0]].add(tiles[1])
        matchingTiles[tiles[1]].add(tiles[0])

print(matchingTiles)

corners = [tile for tile in matchingTiles if len(matchingTiles[tile]) == 2]
print(corners)
assert len(corners) == 4
print(corners[0] * corners[1] * corners[2] * corners[3])
remaining = set(matchingTiles.keys())

def findMatch(t, matches=None):
    for m in remaining:
        if matches is not None:
            if len(matchingTiles[m]) != matches:
                continue
        if t in matchingTiles[m]:
            remaining.remove(m)
            return m

topleft = corners[0]
remaining.remove(topleft)
toprow = [topleft]
while True:
    m = findMatch(toprow[-1], 3)
    if m:
        toprow.append(m)
    else:
        break
topright = findMatch(toprow[-1], 2)
toprow.append(topright)
rows = [toprow]
while True:
    if not remaining:
        break
    row = []
    for t in rows[-1]:
        m = findMatch(t)
        row.append(m)
    rows.append(row)
print(rows)
