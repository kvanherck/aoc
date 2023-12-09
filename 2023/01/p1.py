#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

s = 0
for line in inputLines():
    n = ''
    for c in line:
        if c >= '0' and c <= '9':
            n += c
    print(n)
    s += int(n[0] + n[-1])
print(s)
