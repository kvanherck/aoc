#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *
import numpy as np

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
    n += 1
    m = max(m, len(line))

path = lines[n + 1].strip()

a = np.zeros((n, m), dtype=int)
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c == '.':
            a[i, j] = 1
        elif c == '#':
            a[i, j] = 2

print(a)

def turn(direction, cw):
    if cw:
        return (direction + 1) % 4
    else:
        return (direction - 1) % 4

def move(x, y, direction):
    if direction == RIGHT:
        xx = (x + 1) % m
        if a[y, xx] == 0:
            for xx in range(m):
                if a[y, xx] != 0:
                    break
        if a[y, xx] == 1:
            return xx, y
        else:
            return x, y
    elif direction == LEFT:
        xx = (x - 1) % m
        if a[y, xx] == 0:
            for xx in range(m - 1, 0, -1):
                if a[y, xx] != 0:
                    break
        if a[y, xx] == 1:
            return xx, y
        else:
            return x, y
    if direction == DOWN:
        yy = (y + 1) % n
        if a[yy, x] == 0:
            for yy in range(n):
                if a[yy, x] != 0:
                    break
        if a[yy, x] == 1:
            return x, yy
        else:
            return x, y
    if direction == UP:
        yy = (y - 1) % n
        if a[yy, x] == 0:
            for yy in range(n - 1, 0, -1):
                if a[yy, x] != 0:
                    break
        if a[yy, x] == 1:
            return x, yy
        else:
            return x, y

def walk(x, y, direction, steps):
    for i in range(steps):
        xx, yy = move(x, y, direction)
        if (xx, yy) == (x, y):
            break
        x, y = xx, yy
    return xx, yy

direction = RIGHT
x, y = move(0, 0, direction)
print(f'Starting at ({x}, {y})')

l = 0
for c in path:
    if c == 'R':
        if l:
            x, y = walk(x, y, direction, l)
            print(f'Moved {l} to ({x}, {y})')
        direction = turn(direction, True)
        print(f'Turned to {direction}')
        l = 0
    elif c == 'L':
        if l:
            x, y = walk(x, y, direction, l)
            print(f'Moved {l} to ({x}, {y})')
        direction = turn(direction, False)
        print(f'Turned to {direction}')
        l = 0
    else:
        l *= 10
        l += int(c)
if l:
    x, y = walk(x, y, direction, l)
    print(f'Moved {l} to ({x}, {y})')

score = 1000 * (y + 1) + 4 * (x + 1) + direction
print(score)
