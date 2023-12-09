#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *
import math

lines = list(inputLines())
assert len(lines) == 2

start = int(lines[0])
busses = list(map(int, lines[1].replace('x', '0').split(',')))

# busses = [17,0,13,19]
# busses = [1789,37,47,1889]

def isPrime(n):
	divisors = [d for d in range(2, int(math.sqrt(n))+1) if n % d == 0]
	return divisors == []

start = 0
factor = 1
for i, bus in enumerate(busses):
	if bus != 0:
		assert isPrime(bus)
		while (start + i) % bus != 0:
			start += factor
		factor *= bus
		print(i, bus, start, factor)

print(start)
