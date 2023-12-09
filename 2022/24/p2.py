#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

LEFT = 2
RIGHT = 3
UP = 4
DOWN = 5

lines = inputArray(valueMapping={'.': 0, '#': 1, '<': LEFT, '>': RIGHT, '^': UP, 'v': DOWN})
n = len(lines)
m = len(lines[0])

for j, c in enumerate(lines[0]):
    if c == 0:
        start = (0, j)

for j, c in enumerate(lines[n - 1]):
    if c == 0:
        finish = (n - 1, j)

print(n, m)
print(start)
print(finish)

blizzards = []
for i in range(1, n-1):
    for j in range(1, m-1):
        if lines[i][j] != 0:
            blizzards.append((i, j, lines[i][j]))

def update():
    for p, blizzard in enumerate(blizzards):
        i, j, type = blizzard
        if type == LEFT:
            j -= 1
            if j == 0:
                j = m - 2
        elif type == RIGHT:
            j += 1
            if j == m - 1:
                j = 1
        if type == UP:
            i -= 1
            if i == 0:
                i = n - 2
        elif type == DOWN:
            i += 1
            if i == n - 1:
                i = 1
        blizzards[p] = (i, j, type)

def moves(position, finish):
    s = set()
    for (i, j, type) in blizzards:
        s.add((i, j))
    i, j = position
    r = []
    if position not in s:
        r.append(position)
    if i > 1 or ((i-1, j) == finish):
        if (i-1, j) not in s:
            r.append((i-1, j))
    if i < n-2 or ((i+1, j) == finish):
        if (i+1, j) not in s:
            r.append((i+1, j))
    if i != 0 and i != n-1 and j > 1:
        if (i, j-1) not in s:
            r.append((i, j-1))
    if i != 0 and i != n-1 and j < m-2:
        if (i, j+1) not in s:
            r.append((i, j+1))
    return r

def search(start, finish):
    positions = set([start])
    iteration = 0
    while finish not in positions:
        iteration += 1
        update()
        newPositions = set()
        distance = n + m
        for position in positions:
            for p in moves(position, finish):
                newPositions.add(p)
                i, j = p
                d = n - i + m - j - 2
                distance = min(distance, d)
        positions = newPositions
        print(iteration, len(positions), distance)
    return iteration

iteration1 = search(start, finish)
iteration2 = search(finish, start)
iteration3 = search(start, finish)
print(iteration1 + iteration2 + iteration3)
