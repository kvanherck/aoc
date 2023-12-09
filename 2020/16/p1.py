#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

chunks = list(inputChunks())
assert len(chunks) == 3

fields = {}
allvalues = set()
for line in chunks[0]:
    g = re.match(r'(.+): (\d+)-(\d+) or (\d+)-(\d+)', line).groups()
    name = g[0]
    x = int(g[1])
    y = int(g[2])
    r = list(range(x, y+1))
    x = int(g[3])
    y = int(g[4])
    r += list(range(x, y+1))
    fields[name] = r
    for x in r:
        allvalues.add(x)

print(fields)
print(allvalues)

errors = 0
for line in chunks[2][1:]:
    values = list(map(int, line.split(',')))
    for x in values:
        if x not in allvalues:
            errors += x

print(errors)
