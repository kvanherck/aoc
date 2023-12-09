#!/usr/bin/env python3
import sys
import numpy as np
sys.path.append('..')
from common import *

g = 6 + 1

i = np.asarray(inputArray())
print(i)
n, m = i.shape

newshape = (1 + 2*g, n + 2*g, m + 2*g)
a = np.zeros(newshape, dtype=int)
a[g, g:g+n, g:g+m] = i

for gg in range(1, g):
    na = np.zeros(newshape, dtype=int)
    print('Generation', gg)
    n = a.shape[0]
    for i in range(1, n - 1):
        n = a.shape[1]
        for j in range(1, n - 1):
            n = a.shape[2]
            for k in range(1, n - 1):
                sa = a[i-1:i+2, j-1:j+2, k-1:k+2]
                s = sum(sa.ravel())
                if a[i, j, k] == 1:
                    if s == 3 or s == 4:
                        na[i, j, k] = 1
                else:
                    if s == 3:
                        na[i, j, k] = 1
    print(sum(na.ravel()))
    a = na
