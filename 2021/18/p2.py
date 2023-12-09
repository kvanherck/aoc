#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *
from p1 import parse, reduce, add, magnitude

lines = list(inputLines())
n = len(lines)

mm = 0
for i in range(n):
	for j in range(n):
		if i == j:
			continue
		l1 = parse(lines[i])
		l2 = parse(lines[j])
		l = reduce(add(l1, l2))
		m = magnitude(l)
		mm = max(mm, m)
print(mm)
