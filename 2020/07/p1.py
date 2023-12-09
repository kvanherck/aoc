#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

result = 0
rules = {}
for bag, others in inputRE(r'^(.+) bags contain (.+).$'):
    otherBags = {}
    if others != 'no other bags':
        for other in others.split(', '):
            m = re.match(r'(\d+) (.+) bag', other)
            if m:
                n = int(m.group(1))
                otherBag = m.group(2)
                otherBags[otherBag] = n
    rules[bag] = otherBags

for k, v in rules.items():
    print(k, 'contains', v)

def checkBag(bag):
    contains = rules[bag]
    if not contains:
        return False
    else:
        for other in contains:
            if other == 'shiny gold':
                return True
            else:
                if checkBag(other):
                    return True
        return False

cnt = 0
for bag in rules:
    r = checkBag(bag)
    if r:
        cnt += 1
    print(bag, r)

print(cnt)
