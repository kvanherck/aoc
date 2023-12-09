#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *
import numpy as np

VOID = 0
FREE = 1
WALL = 2

RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3

n = m = 0
lines = list(inputLines(stripWhitespace=False))
for line in lines:
    if line.endswith('\n'):
        line = line[:-1]
    if len(line) == 0:
        break
    start = 0
    while line[start] == ' ':
        start += 1
    end = start
    while end < len(line) and line[end] != ' ':
        end += 1
    print(n, start, end)
    n += 1
    m = max(m, len(line))

path = lines[n + 1].strip()

a = np.zeros((n, m), dtype=int)
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c == '.':
            a[i, j] = FREE
        elif c == '#':
            a[i, j] = WALL

if len(sys.argv) == 2:
    rightEdges = []
    for y in range(0, 4):
        rightEdges.append((12, (15, 11-y, LEFT)))
    for y in range(4, 8):
        rightEdges.append((12, (15-y+4, 8, DOWN)))
    for y in range(8, 12):
        rightEdges.append((16, (11, 11-y, LEFT)))
    leftEdges = []
    for y in range(0, 4):
        leftEdges.append((7, (4+y, 4, DOWN)))
    for y in range(4, 8):
        leftEdges.append((-1, (15-y+4, 11, UP)))
    for y in range(8, 12):
        leftEdges.append((7, (15-y, 7, UP)))
    upEdges = []
    for x in range(0, 4):
        upEdges.append((3, (11-x, 0, DOWN)))
    for x in range(4, 8):
        upEdges.append((3, (8, x-4, RIGHT)))
    for x in range(8, 12):
        upEdges.append((-1, (11-x, 0, DOWN)))
    for x in range(12, 16):
        upEdges.append((7, (11, 7-x+12, LEFT)))
    downEdges = []
    for x in range(0, 4):
        downEdges.append((8, (11-x, 11, UP)))
    for x in range(4, 8):
        downEdges.append((8, (8, 11-x+4, RIGHT)))
    for x in range(8, 12):
        downEdges.append((12, (11-x, 7, UP)))
    for x in range(12, 16):
        downEdges.append((12, (0, 7-x+12, RIGHT)))
else:
    rightEdges = []
    for y in range(0, 50):
        rightEdges.append((150, (99, 149-y, LEFT)))
    for y in range(50, 100):
        rightEdges.append((100, (y+50, 49, UP)))
    for y in range(100, 150):
        rightEdges.append((100, (149, 149-y, LEFT)))
    for y in range(150, 200):
        rightEdges.append((50, (y-100, 149, UP)))
    leftEdges = []
    for y in range(0, 50):
        leftEdges.append((49, (0, 149-y, RIGHT)))
    for y in range(50, 100):
        leftEdges.append((49, (y-50, 100, DOWN)))
    for y in range(100, 150):
        leftEdges.append((-1, (50, 149-y, RIGHT)))
    for y in range(150, 200):
        leftEdges.append((-1, (y-100, 0, DOWN)))
    upEdges = []
    for x in range(0, 50):
        upEdges.append((99, (50, x+50, RIGHT)))
    for x in range(50, 100):
        upEdges.append((-1, (0, x+100, RIGHT)))
    for x in range(100, 150):
        upEdges.append((-1, (x-100, 199, UP)))
    downEdges = []
    for x in range(0, 50):
        downEdges.append((200, (x+100, 0, DOWN)))
    for x in range(50, 100):
        downEdges.append((150, (49, x+100, LEFT)))
    for x in range(100, 150):
        downEdges.append((50, (99, x-50, LEFT)))

def turn(direction, cw):
    if cw:
        return (direction + 1) % 4
    else:
        return (direction - 1) % 4

def next(x, y, direction):
    xx, yy, dd = x, y, direction
    if direction == RIGHT:
        xx = x + 1
        if rightEdges[yy][0] == xx:
            xx, yy, dd = rightEdges[yy][1]
    elif direction == LEFT:
        xx = x - 1
        if leftEdges[yy][0] == xx:
            xx, yy, dd = leftEdges[yy][1]
    elif direction == DOWN:
        yy = y + 1
        if downEdges[xx][0] == yy:
            xx, yy, dd = downEdges[xx][1]
    elif direction == UP:
        yy = y - 1
        if upEdges[xx][0] == yy:
            xx, yy, dd = upEdges[xx][1]
    return xx, yy, dd

def walk(x, y, direction, steps):
    d = direction
    for i in range(steps):
        xx, yy, dd = next(x, y, d)
        assert a[yy, xx] != VOID
        if a[yy, xx] == WALL:
            break
        x, y, d = xx, yy, dd
    return x, y, d

def findStart():
    x, y, d = 0, 0, RIGHT
    while a[y, x] == VOID:
        x += 1
    return x, y, d

x, y, direction = findStart()
print(f'Starting at ({x}, {y})')

l = 0
for c in path:
    if c == 'R':
        if l:
            x, y, direction = walk(x, y, direction, l)
            print(f'Moved {l} to ({x}, {y})')
        direction = turn(direction, True)
        print(f'Turned to {direction}')
        l = 0
    elif c == 'L':
        if l:
            x, y, direction = walk(x, y, direction, l)
            print(f'Moved {l} to ({x}, {y})')
        direction = turn(direction, False)
        print(f'Turned to {direction}')
        l = 0
    else:
        l *= 10
        l += int(c)
if l:
    x, y, direction = walk(x, y, direction, l)
    print(f'Moved {l} to ({x}, {y})')

score = 1000 * (y + 1) + 4 * (x + 1) + direction
print(score)
