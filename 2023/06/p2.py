#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *
from math import sqrt, floor, ceil

lines = list(inputLines())
time = int(lines[0].split(':')[1].replace(' ', ''))
distance = int(lines[1].split(':')[1].replace(' ', ''))
print(time)
print(distance)

# distance = x * (t - x) for x = 0 .. t
# x * (t - x) = d
# x*x - t*x + d = 0
# x1, x2 = (t +/- sqrt(t*t - 4*d)) / 2
d = sqrt(time*time - 4*distance)
x1 = (time - d)/2
x2 = (time + d)/2
x1 = ceil(x1)
x2 = floor(x2)
if x1 * (time - x1) == distance:
    x1 += 1
if x2 * (time - x2) == distance:
    x2 -= 1
s = x2 - x1 + 1
print(s)
