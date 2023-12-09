#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *
from math import prod

score = 0
for line in inputLines():
    fields = line.split(':')
    game = int(fields[0][5:])
    draws = fields[1].split(';')
    counts = {'red': 0, 'green': 0, 'blue': 0}
    for draw in draws:
        cubes = draw.strip().split(',')
        for cube in cubes:
            n, color = cube.strip().split(' ')
            n = int(n)
            counts[color] = max(counts[color], n)
    power = prod(counts.values())
    score += power

print(score)
