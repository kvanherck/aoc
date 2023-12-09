#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

cnt = 0
for chunk in inputChunks():
    intersection = None
    for line in chunk:
        s = set(list(line))
        if intersection is None:
            intersection = s
        else:
            intersection &= s
    print(len(intersection), chunk, intersection)
    cnt += len(intersection)
print(cnt)
