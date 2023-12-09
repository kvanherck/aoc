#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *
import numpy as np

a = np.zeros((102, 102, 102), dtype=int)
for fields in inputRE(r'(on|off) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)'):
    state = int(fields[0] == 'on')
    fields = map(int, fields[1:])
    fields = [51+max(-51, min(51, f)) for f in fields]
    x1, x2, y1, y2, z1, z2 = fields
    print(state, x1, x2, y1, y2, z1, z2)
    a[x1:x2+1, y1:y2+1, z1:z2+1] = state

print(np.sum(a[1:101, 1:101, 1:101]))
