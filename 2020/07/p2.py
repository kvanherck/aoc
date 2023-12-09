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

cache = {}
def checkBag(bag):
    try:
        return cache[bag]
    except KeyError:
        r = sum([checkBag(other) * n for other, n in rules[bag].items()]) + 1
        print(f'{bag} accounts for {r} bags')
        cache[bag] = r
        return r

print(checkBag('shiny gold') - 1)
