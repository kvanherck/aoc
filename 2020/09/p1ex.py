#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

l = []
for i in inputInts():
    l.append(i)

def check(l, n):
    s = set(l)
    for x in s:
        if n - x in s:
            return True
    return False

preamble = 5
i = 0
while i + preamble < len(l):
    ll = l[i:i+preamble]
    if not check(ll, l[i + preamble]):
        print(l[i + preamble])
        break
    i += 1
