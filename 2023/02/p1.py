#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

score = 0
maxCounts = {'red': 12, 'green': 13, 'blue': 14}
for line in inputLines():
    fields = line.split(':')
    game = int(fields[0][5:])
    draws = fields[1].split(';')
    valid = True
    for draw in draws:
        cubes = draw.strip().split(',')
        for cube in cubes:
            n, color = cube.strip().split(' ')
            n = int(n)
            if n > maxCounts[color]:
                valid = False
    if valid:
        score += game

print(score)
