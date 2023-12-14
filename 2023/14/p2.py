#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

grid = inputGrid()

def tiltNorth():
    for j in range(grid.m):
        for i in range(grid.n):
            if grid[i, j] == 'O':
                k = i - 1
                while grid[k, j] == '.':
                    grid[k, j] = 'O'
                    grid[k + 1, j] = '.'
                    k -= 1

def tiltSouth():
    for j in range(grid.m):
        for i in range(grid.n - 1, -1, -1):
            if grid[i, j] == 'O':
                k = i + 1
                while grid[k, j] == '.':
                    grid[k, j] = 'O'
                    grid[k - 1, j] = '.'
                    k += 1

def tiltWest():
    for i in range(grid.n):
        for j in range(grid.m):
            if grid[i, j] == 'O':
                k = j - 1
                while grid[i, k] == '.':
                    grid[i, k] = 'O'
                    grid[i, k + 1] = '.'
                    k -= 1

def tiltEast():
    for i in range(grid.n):
        for j in range(grid.m - 1, -1, -1):
            if grid[i, j] == 'O':
                k = j + 1
                while grid[i, k] == '.':
                    grid[i, k] = 'O'
                    grid[i, k - 1] = '.'
                    k += 1

def cycle():
    tiltNorth()
    tiltWest()
    tiltSouth()
    tiltEast()

def rocks():
    rocks = []
    for i in range(grid.n):
        for j in range(grid.m):
            if grid[i, j] == 'O':
                rocks.append((i, j))
    return tuple(rocks)

def score(r):
    score = 0
    for i, j in r:
        score += grid.n - i
    return score

history = [rocks()]
rocksSeen = {rocks(): 0}
cycles = 0
target = 1000000000
while cycles < target:
    cycle()
    cycles += 1
    r = rocks()
    print(cycles, score(r))
    if r in rocksSeen:
        break
    history.append(r)
    rocksSeen[r] = cycles

k = rocksSeen[r]
n = cycles - k
print(f'Repeats every {n} from {k} to {cycles}')
m = k + (target - k) % n
print(f'{target} = {m}')
r = history[m]
print(score(r))
