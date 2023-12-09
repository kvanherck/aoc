#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *
import numpy as np

i = np.asarray(inputArray(valueMapping={'0': 0, '1': 1}))
print(i)

n, m = i.shape
s = sum(i)
g = (s > n/2) * 1
print(g)

p2 = (2 ** np.arange(m))[::-1]
gamma = sum(g * p2)
mask = (1 << m) - 1
epsilon = gamma ^ mask

print(gamma, epsilon, gamma * epsilon)
