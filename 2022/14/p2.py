#!/usr/bin/env python3
import sys
sys.path.append('..')
import numpy as np
from common import *

coords = []
xs = [500]
ys = [0]
for line in inputLines():
    rock = []
    chunks = line.split(' -> ')
    for chunk in chunks:
        x, y = map(int, chunk.split(','))
        xs.append(x)
        ys.append(y)
        rock.append((x, y))
    coords.append(rock)

print(f'Input range: X:{min(xs)}-{max(xs)} Y:{min(ys)}-{max(ys)}')
xoffset = min(xs) - max(ys)
assert min(ys) == 0
n = max(ys) + 2
m = max(xs) - xoffset + 1 + max(ys)
print(f'Array size: ({n}, {m})')
a = np.zeros((n, m), dtype=int)

def plot():
    charMap = {
        0: ' ',
        1: '#',
        2: '.',
    }
    for i in range(n):
        line = ''
        for j in range(m):
            line += charMap[a[i, j]]
        print(line)

for rock in coords:
    x0, y0 = rock.pop(0)
    while rock:
        x, y = rock.pop(0)
        if x == x0:
            if y0 <= y:
                for i in range(y0, y+1):
                    a[i, x0 - xoffset] = 1
            else:
                for i in range(y, y0+1):
                    a[i, x0 - xoffset] = 1
        elif y == y0:
            if x0 <= x:
                for i in range(x0, x+1):
                    a[y0, i - xoffset] = 1
            else:
                for i in range(x, x0+1):
                    a[y0, i - xoffset] = 1
        else:
            assert False
        x0, y0 = x, y

plot()

cnt = 0
done = False
while not done:
    x, y = (500 - xoffset, 0)
    while True:
        if a[y+1, x] == 0:
            x, y = x, y+1
        elif a[y+1, x-1] == 0:
            x, y = x-1, y+1
        elif a[y+1, x+1] == 0:
            x, y = x+1, y+1
        else:
            a[y, x] = 2
            cnt += 1
            if (x, y) == (500 - xoffset, 0):
                done = True
            break
        if y == n - 1:
            a[y, x] = 2
            cnt += 1
            break

print()
plot()
print()
print(cnt)
