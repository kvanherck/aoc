#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

l = []
for i in inputInts():
    l.append(i)

l.sort()
l.append(l[-1] + 3)

p = 0
d1 = 0
d2 = 0
d3 = 0
for x in l:
    # print(p, x)
    if x - p == 1:
        d1 += 1
    elif x - p == 2:
        d2 += 1
    elif x - p == 3:
        d3 += 1
    else:
        print('error', p, x)
        break
    p = x

print(d1, d2, d3, d1 * d3)
