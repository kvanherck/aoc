#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

score = 0
for line in inputLines():
    sections = line.split(',')
    s1, e1 = map(int, sections[0].split('-'))
    s2, e2 = map(int, sections[1].split('-'))
    if s1 <= s2 and e1 >= e2:
        score += 1
    elif s2 <= s1 and e2 >= e1:
        score += 1

print(score)
