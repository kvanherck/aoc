#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

foods = []
a2i = {}
alli = set()
for ingredients, allergenes in inputRE(r'(.+) \(contains (.+)\)'):
    ingredients = ingredients.split()
    allergenes = allergenes.split(', ')
    foods.append((ingredients, allergenes))
    alli |= set(ingredients)
    for a in allergenes:
        s = set(ingredients)
        if a not in a2i:
            a2i[a] = s
        else:
            a2i[a] &= s

foundi = set()
for a, i in a2i.items():
    foundi |= i
notfound = alli - foundi

cnt = 0
for ings, algs in foods:
    for ing in ings:
        if ing in notfound:
            cnt += 1
print(cnt)
