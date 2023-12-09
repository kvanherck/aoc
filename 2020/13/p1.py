#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

lines = list(inputLines())
assert len(lines) == 2

start = int(lines[0])
busses = list(map(int, lines[1].replace('x', '0').split(',')))
busses = [bus for bus in busses if bus != 0]

print(start)
print(busses)

results = []
for bus in busses:
    m = start % bus
    if m != 0:
        wait = bus - m
    else:
        wait = 0
    depart = start + wait
    results.append((depart, bus, wait))
    print(bus, depart)

results.sort()
print(results[0])
print(results[0][1] * results[0][2])
