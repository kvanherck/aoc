#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

prev = None
incs = 0
for i in inputInts():
    if prev is not None:
        if i > prev:
            incs += 1
    prev = i

print(incs)
