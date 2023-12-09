#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

l = list(inputInts())

prev = None
incs = 0
for i in range(len(l) - 2):
    s = sum(l[i:i+3])
    if prev is not None:
        if s > prev:
            incs += 1
    prev = s

print(incs)
