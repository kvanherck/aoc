#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *
import numpy as np
import re

line = list(inputLines())[0]
fields = re.search(r'x=([\-\d]+)\.\.([\-\d]+), y=([\-\d]+)\.\.([\-\d]+)', line).groups()
a, b, c, d = map(int, fields)
print(a, b, c, d)

def solve():
	hmax = 0
	cnt = 0
	for xvol0 in range(1, b+1):
		for yvol0 in range(c, -c):
			xvol, yvol = xvol0, yvol0
			h = 0
			x, y = 0, 0
			while x <= b and y >= c:
				h = max(h, y)
				if a <= x and x <= b and c <= y and y <= d:
					cnt += 1
					if h > hmax:
						hmax = h
						print(xvol0, yvol0, hmax)
					break
				x += xvol
				y += yvol
				if xvol > 0:
					xvol -= 1
				yvol -= 1
	print(cnt)

solve()
