#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

score = 0
for line in inputLines():
    sections = line.split(',')
    s1, e1 = map(int, sections[0].split('-'))
    s2, e2 = map(int, sections[1].split('-'))
    if not (s2 > e1 or s1 > e2):
        score += 1

print(score)
