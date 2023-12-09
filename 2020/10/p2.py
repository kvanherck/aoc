#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

l = []
for i in inputInts():
    l.append(i)

l.sort()
l.append(l[-1] + 3)
print(l)

deltas = []
p = 0
for x in l:
    deltas.append(x - p)
    p = x
print(deltas)

# delta = 1 1 3
# (0) 1 2 (5)
# (0)   2 (5)
# ==> 2 combos

# delta = 1 1 1 3
# (0) 1 2 3 (6)
# (0)   2 3 (6)
# (0) 1   3 (6)
# (0)     3 (6)
# ==> 4 combos

# delta = 1 1 1 1 3
# (0) 1 2 3 4 (7)
# (0)   2 3 4 (7)
# (0) 1   3 4 (7)
# (0)     3 4 (7)
# (0) 1 2   4 (7)
# (0)   2   4 (7)
# (0) 1     4 (7)
# ==> 7 combos

n1 = 0
c = 1
for d in deltas:
    if d == 1:
        n1 += 1
    elif d == 3:
        if n1 == 0 or n1 == 1:
            pass
        elif n1 == 2:
            c *= 2
        elif n1 == 3:
            c *= 4
        elif n1 == 4:
            c *= 7
        else:
            print('Invalid n1:', n1)
        n1 = 0
print(c)
