#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

a2i = {}
for ingredients, allergenes in inputRE(r'(.+) \(contains (.+)\)'):
    ingredients = ingredients.split()
    allergenes = allergenes.split(', ')
    for a in allergenes:
        s = set(ingredients)
        if a not in a2i:
            a2i[a] = s
        else:
            a2i[a] &= s

solved = []
while True:
    if not a2i:
        break
    for a, ings in a2i.items():
        if len(ings) == 1:
            ing = ings.pop()
            solved.append((a, ing))
            del a2i[a]
            for b in a2i:
                a2i[b] -= set([ing])
            break
solved.sort()
print(','.join([i for a, i in solved]))
