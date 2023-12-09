#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

verbose = len(sys.argv) > 1
input = [x * 811589153 for x in inputInts()]
if verbose:
    print(input)
n = len(input)
contents = list(range(n))

def round():
    global contents
    for i, x in enumerate(input):
        p = contents.index(i)
        if x != 0:
            if x > 0:
                np = (p + x) % (n - 1)
            else:
                np = (p + x) % (n - 1)
                if np == 0:
                    np = n
            if np > p:
                contents = contents[:p] + contents[p+1:np+1] + [i] + contents[np+1:]
            elif np < p:
                contents = contents[:np] + [i] + contents[np:p] + contents[p+1:]

for i in range(10):
    print(f'Round {i+1}')
    round()
    if verbose:
        print(list([input[k] for k in contents]))

i0 = input.index(0)
p0 = contents.index(i0)
score = 0
for i in [1000, 2000, 3000]:
    x = input[contents[(p0+i) % n]]
    if verbose:
        print(f'{i}: {x}')
    score += x
print(score)
