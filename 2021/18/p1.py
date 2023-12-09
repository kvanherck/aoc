#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

def parse(s):
	values = []
	level = 0
	for c in s:
		if c == '[':
			level += 1
		elif c == ']':
			level -= 1
		elif c == ',':
			pass
		else:
			d = int(c)
			values.append((level, d))
	return values

def reduce(l):
	l = l[:]
	done = False
	while not done:
		done = True
		for i in range(len(l) - 1):
			n1, x1 = l[i]
			n2, x2 = l[i+1]
			if n1 == 5 and n2 == 5:
				if i > 0:
					l[i-1] = (l[i-1][0], l[i-1][1] + x1)
				if i < len(l) - 2:
					l[i+2] = (l[i+2][0], l[i+2][1] + x2)
				l[i:i+2] = [(n1-1, 0)]
				done = False
				break
		if done:
			for i in range(len(l)):
				n, x = l[i]
				if x >= 10:
					x1 = x // 2
					x2 = x - x1
					n1 = n2 = n + 1
					l[i:i+1] = [(n1, x1), (n2, x2)]
					done = False
					break
	return l

def add(l1, l2):
	l = []
	for n, x in l1 + l2:
		l.append(((n+1), x))
	return l

def magnitude(l):
	done = False
	while not done:
		done = True
		for i in range(len(l) - 1):
			n1, x1 = l[i]
			n2, x2 = l[i+1]
			if n1 == n2:
				m = 3*x1 + 2*x2
				l[i:i+2] = [(n1-1, m)]
				done = False
				break
	return m

def main():
	l = None
	for line in inputLines():
		l2 = parse(line)
		if l is None:
			l = l2
		else:
			l = reduce(add(l, l2))
		print(l)
	print(magnitude(l))

if __name__ == '__main__':
	main()
