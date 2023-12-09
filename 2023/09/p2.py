#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *
import numpy as np

score = 0
for line in inputLines():
    a = np.array(list(map(int, line.split())), dtype=int)
    a = a[::-1]
    trace = []
    while not np.all(a == 0):
        trace.append(a[-1])
        a = a[1:] - a[:-1]
    score += np.sum(trace)

print(score)
