#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *
import numpy as np

a = np.asarray(inputArray())
directions = ['N', 'S', 'W', 'E']

def round(a):
    moves = {}
    targets = {}

    def propose(i, j, k, l):
        cnt = targets.get((k, l), 0)
        cnt += 1
        targets[(k, l)] = cnt
        moves[(i, j)] = (k, l)

    n, m = a.shape
    for i in range(n):
        for j in range(m):
            if a[i][j] == 0:
                continue
            if a[i-1:i+2, j-1:j+2].sum() == 1:
                continue
            for d in directions:
                if (i, j) in moves:
                    break
                if d == 'N':
                    if a[i-1, j-1:j+2].sum() == 0:
                        propose(i, j, i-1, j)
                if d == 'S':
                    if a[i+1, j-1:j+2].sum() == 0:
                        propose(i, j, i+1, j)
                if d == 'E':
                    if a[i-1:i+2, j+1].sum() == 0:
                        propose(i, j, i, j+1)
                if d == 'W':
                    if a[i-1:i+2, j-1].sum() == 0:
                        propose(i, j, i, j-1)

    cnt = 0
    for (i, j), (k, l) in moves.items():
        if targets[(k, l)] == 1:
            a[i, j] = 0
            a[k, l] = 1
            cnt += 1

    d = directions.pop(0)
    directions.append(d)

    return cnt

def boundingBox(a):
    x = set()
    y = set()
    for i in range(n):
        for j in range(m):
            if a[i, j] == 1:
                x.add(j)
                y.add(i)
    return (max(x) - min(x) + 1) * (max(y) - min(y) + 1)

def expand(a):
    if a[:, 0].sum() != 0:
        n, m = a.shape
        z = np.zeros((n, m+1))
        z[:, 1:] = a
        a = z
    if a[:, -1].sum() != 0:
        n, m = a.shape
        z = np.zeros((n, m+1))
        z[:, :m] = a
        a = z
    if a[0, :].sum() != 0:
        n, m = a.shape
        z = np.zeros((n+1, m))
        z[1:, :] = a
        a = z
    if a[-1, :].sum() != 0:
        n, m = a.shape
        z = np.zeros((n+1, m))
        z[:n, :] = a
        a = z
    return a

rounds = 0
while True:
    rounds += 1
    a = expand(a)
    cnt = round(a)
    print(f'Round {rounds} had {cnt} moves (shape = {a.shape})')
    if cnt == 0:
        break

print(rounds)
