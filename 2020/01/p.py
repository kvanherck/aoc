#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

s = set()
for i in inputInts():
    if i in s:
        print(f'Found duplicate {i}')
    s.add(i)
print(f'Got {len(s)} unique numbers')

l = list(s)
l.sort()

print('Part A')
for i in l:
    c = 2020 - i
    if c in s:
        print(f'{i} + {c} = 2020, {i} * {c} = {i*c}')
    if i > 1010:
        break

print('Part B')
for i in l:
    for j in l:
        if j > i:
            break
        k = 2020 - i - j
        if k in s:
            print(f'{i} + {j} + {k} = 2020, {i} * {j} * {k} = {i*j*k}')
