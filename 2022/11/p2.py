#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *
from input import monkeys

modulus = 1
for monkey in monkeys:
    modulus *= monkey.divider

def turn(monkey):
    monkey.inspections += len(monkey.items)
    for item in monkey.items:
        worry = monkey.operation(item) % modulus
        target = monkey.targets[worry % monkey.divider != 0]
        monkeys[target].items.append(worry)
        monkey.items = []

for round in range(10000):
    for monkey in monkeys:
        turn(monkey)

inspections = []
for monkey in monkeys:
    inspections.append(monkey.inspections)
    print(monkey.inspections)

inspections.sort()
print(inspections[-1] * inspections[-2])
