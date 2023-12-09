#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

def fuel(m):
	return max(m // 3 - 2, 0)

s = 0
for m in inputInts():
	f = fuel(m)
	tf = f
	while f > 0:
		f = fuel(f)
		tf += f
	s += tf
	print(m, tf)
print(s)
