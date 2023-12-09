#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

hor = 0
ver = 0
for line in inputLines():
    fields = line.split()
    assert len(fields) == 2
    a = fields[0]
    n = int(fields[1])
    if a == 'forward':
        hor += n
    elif a == 'down':
        ver += n
    elif a == 'up':
        ver -= n

print(hor, ver, hor*ver)
