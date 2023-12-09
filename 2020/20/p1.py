#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *
import numpy as np

tiles = {}
edge2tile = {}

valueMapping={'.': 0, '#': 1}

chunks = inputChunks()
for chunk in chunks:
    header = chunk[0]
    fields = header.split()
    n = int(fields[1][:-1])
    rows = []
    for line in chunk[1:]:
        values = [valueMapping[x] for x in line]
        rows.append(values)
    a = np.asarray(rows)
    edges = set()
    print(n)
    print(a)
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

matchingTiles = {}
for edge, tiles in edge2tile.items():
    print(edge, len(tiles), tiles)
    assert len(tiles) in [1, 2], len(tiles)
    if len(tiles) == 2:
        for tile in tiles:
            m = matchingTiles.get(tile, 0)
            m += 1
            matchingTiles[tile] = m

print(matchingTiles)

corners = [tile for tile in matchingTiles if matchingTiles[tile] == 4]
print(corners)
assert len(corners) == 4
print(corners[0] * corners[1] * corners[2] * corners[3])
