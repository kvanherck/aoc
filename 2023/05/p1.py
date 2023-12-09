#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

chunks = list(inputChunks())
sources = set(map(int, chunks[0][0].split()[1:]))
print(sources)

for chunk in chunks[1:]:
    targets = set()
    print(chunk[0])
    for line in chunk[1:]:
        target, source, count = tuple(map(int, line.split()))
        for x in list(sources):
            if x >= source and x < source + count:
                y = x - source + target
                targets.add(y)
                sources.remove(x)
    targets |= sources
    print(targets)
    sources = targets

print(min(targets))
