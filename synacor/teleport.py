#!/usr/bin/env python3
from timeit import default_timer as timer
import numpy as np

def f(r0, r1, r7):
    if r0 == 0:
        return r1 + 1, r1
    if r1 == 0:
        return f(r0 - 1, r7, r7)
    r1, _ = f(r0, r1 - 1, r7)
    return f(r0 - 1, r1, r7)

# f(0, r1) = r1 + 1

# f(1, 0) = f(0, r7) = r7 + 1
# f(1, r1) = f(0, f(1, r1-1)) = f(1, r1-1) + 1 = r7 + r1 + 1

# f(2, 0) = f(1, r7) = 2*r7 + 1
# f(2, r1) = f(1, f(2, r1-1)) = f(2, r1-1) + r7 + 1 = r1*(r7 + 1) + 2*r7 + 1 = (r1 + 2)*r7 + r1 + 1

def f2table(r7):
    r1 = np.arange(0x8000, dtype=np.int16)
    x = ((r1 + 2) * r7 + r1 + 1) % 0x8000
    return x

def f3(r1, r7, f2t):
    x = r7
    for i in range(r1+1):
        x = f2t[x]
    return x

def f4(r1, r7):
    f2t = f2table(r7)
    x = r7
    for i in range(r1+1):
        x = f3(x, r7, f2t)
    return x

# Sanity check
for r7 in range(1, 5):
    f2t = f2table(r7)
    for r1 in range(2):
        x, y = f(3, r1, r7)
        print(3, r1, r7, x)
        assert x == f3(r1, r7, f2t)

# Search r7 such that f(4, 1, r7) == 6
for r7 in range(0x8000):
    x = f4(1, r7)
    if r7 % 100 == 0:
        print(4, 1, r7, x)
    if x == 6:
        print(4, 1, r7, x)
        break
else:
    print('No solution found')
