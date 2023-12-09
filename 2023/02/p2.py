#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *
from math import prod

score = 0
for line in inputLines():
    counts = {}
    for draw in line.strip().split(': ')[1].split('; '):
        for cubes in draw.split(', '):
            count, color = cubes.split(' ')
            counts[color] = max(counts.get(color, 0), int(count))
    score += prod(counts.values())
print(score)
