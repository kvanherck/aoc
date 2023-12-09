#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *
import numpy as np

numberOfRocks = 2022
pattern = list(inputLines())[0].strip()
patternLength = len(pattern)
patternIndex = 0

a = np.zeros((numberOfRocks * 4, 7), dtype=int)
height = 0

widths = {
    0: 4,
    1: 3,
    2: 3,
    3: 1,
    4: 2
}

heights = {
    0: 1,
    1: 3,
    2: 3,
    3: 4,
    4: 2
}

def overlaps(rockType, x, y):
    if y < 0:
        return True
    if x < 0:
        return True
    if x + widths[rockType] > 7:
        return True
    if rockType == 0:
        if a[y, x:x+4].sum() != 0:
            return True
    elif rockType == 1:
        if a[y+1, x:x+3].sum() != 0:
            return True
        if a[y:y+3, x+1].sum() != 0:
            return True
    elif rockType == 2:
        if a[y, x:x+3].sum() != 0:
            return True
        if a[y:y+3, x+2].sum() != 0:
            return True
    elif rockType == 3:
        if a[y:y+4, x].sum() != 0:
            return True
    elif rockType == 4:
        if a[y:y+2, x:x+2].sum() != 0:
            return True
    return False

def addRock(rockType, x, y):
    if rockType == 0:
        a[y, x:x+4] = 1
    elif rockType == 1:
        a[y+1, x:x+3] = 1
        a[y:y+3, x+1] = 1
    elif rockType == 2:
        a[y, x:x+3] = 1
        a[y:y+3, x+2] = 1
    elif rockType == 3:
        a[y:y+4, x] = 1
    elif rockType == 4:
        a[y:y+2, x:x+2] = 1

def show():
    for i in range(height, -1, -1):
        line = []
        for j in range(7):
            line.append('#' if a[i, j] else '.')
        print(''.join(line))

for rock in range(numberOfRocks):
    print(f'Processing rock {rock+1}')
    rockType = rock % 5
    x = 2
    y = height + 3
    while True:
        # print(rock, patternIndex, rockType, x, y)
        movement = pattern[patternIndex]
        patternIndex = (patternIndex + 1) % patternLength
        if movement == '<':
            if not overlaps(rockType, x-1, y):
                x -= 1
        else:
            if not overlaps(rockType, x+1, y):
                x += 1
        if overlaps(rockType, x, y-1):
            addRock(rockType, x, y)
            newHeight = y + heights[rockType]
            height = max(height, newHeight)
            break
        y -= 1

show()
print()
print(height)
