#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *
import numpy as np

numberOfSegments = {
    0: 6,
    1: 2,
    2: 5,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 6,
}

uniqueSegments = {
    1: 2,
    4: 4,
    7: 3,
    8: 7,
}

cnt = 0
for line in inputLines():
    parts = line.split('|')
    assert len(parts) == 2
    for word in parts[1].split():
        if len(word) in [2, 3, 4, 7]:
            cnt += 1

print(cnt)
