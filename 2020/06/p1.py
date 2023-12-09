#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

cnt = 0
for chunk in inputChunks():
    s = set()
    for line in chunk:
        for c in line:
            s.add(c)
    print(len(s), chunk)
    cnt += len(s)
print(cnt)
