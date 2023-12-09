#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *
from functools import cmp_to_key
from p1 import compare

i1 = 1
i2 = 2
for line in inputLines():
    if not line:
        continue
    packet = eval(line)
    if compare(packet, [[2]]):
        i1 += 1
    if compare(packet, [[6]]):
        i2 += 1

print(i1 * i2)
