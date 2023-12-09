#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *
import numpy as np
import p1

a = p1.readInput()
n, m = a.shape

b = np.zeros((5*n, 5*m), dtype=int)
for j in range(5):
	b[0:n, j*m:(j+1)*m] = a
	a += np.ones((n, m), dtype=int)
	a[a == 10] = 1

a = b[0:n, :].copy()
for i in range(1, 5):
	a += np.ones((n, 5*m), dtype=int)
	a[a == 10] = 1
	b[i*n:(i+1)*n, :] = a

print(b)
n, m = b.shape
print(n, m, n*m)
print(p1.dijkstra(b, (0, 0), (n-1, m-1)))
