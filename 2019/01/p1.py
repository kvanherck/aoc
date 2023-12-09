#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

def fuel(m):
	return m // 3 - 2

s = 0
for m in inputInts():
	f = fuel(m)
	s += f
	print(m, f)
print(s)
