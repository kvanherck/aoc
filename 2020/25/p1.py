#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

m = 20201227

def operation(x, s, n):
    return x * pow(s, n, m) % m
    for i in range(n):
        x *= s
        x = x % m
    return x

def findN(y):
    n = 1
    x = 1
    while True:
        x = x * 7 % m
        if x == y:
            return n
        n += 1

def findKey(x, y):
    xn = findN(x)
    print(x, xn)

    yn = findN(y)
    print(y, yn)

    k = operation(1, x, yn)
    l = operation(1, y, xn)
    assert k == l
    return k

print(findKey(5764801, 17807724))

l = list(inputInts())
assert len(l) == 2
print(findKey(l[0], l[1]))
