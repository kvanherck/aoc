#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

l = []
for i in inputInts():
    l.append(i)

n = 127
for i in range(len(l)):
    j = 1
    while i + j <= len(l):
        r = l[i:i+j]
        s = sum(r)
        if s == n:
            print(i, j, min(r), max(r))
            break
        if s > n:
            break
        j += 1
