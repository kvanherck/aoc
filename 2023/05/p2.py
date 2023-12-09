#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

chunks = list(inputChunks())
sources = list(map(int, chunks[0][0].split()[1:]))
sources = set(zip(sources[::2], sources[1::2]))

print(len(sources))

for chunk in chunks[1:]:
    targets = set()
    print(chunk[0])
    for line in chunk[1:]:
        target, source, count = tuple(map(int, line.split()))
        for x, n in list(sources):
            if source <= x and source + count >= x + n:
                sources.remove((x, n))
                targets.add((target + x - source, n))
            if source <= x and source + count > x and source + count < x + n:
                m = source + count - x
                sources.remove((x, n))
                sources.add((x + m, n - m))
                targets.add((target + x - source, m))
            if source > x and source < x + n and source + count >= x + n:
                m = x + n - source
                sources.remove((x, n))
                sources.add((x, n - m))
                targets.add((target, m))
            if source > x and source + count < x + n:
                m = count
                sources.remove((x, n))
                sources.add((x, source - x))
                sources.add((x + m, x + n - target - count))
                targets.add((target, m))
    targets |= sources
    print(len(targets))
    sources = targets

print(min(targets)[0])
