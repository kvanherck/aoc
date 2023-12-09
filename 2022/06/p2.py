#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

n = 14

for line in inputLines():
    for i in range(len(line)):
        s = set(line[i:i+n])
        if len(s) == n:
            print(i + n)
            break
