#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *
from example import monkeys

def turn(monkey):
    print(monkey.items)
    monkey.inspections += len(monkey.items)
    for item in monkey.items:
        worry = monkey.operation(item) // 3
        target = monkey.targets[worry % monkey.divider != 0]
        monkeys[target].items.append(worry)
        monkey.items = []
        print(f'Item {item} becomes {worry} goes to {target}')

for round in range(20):
    for monkey in monkeys:
        turn(monkey)

inspections = []
for monkey in monkeys:
    inspections.append(monkey.inspections)
    print(monkey.inspections, monkey.items)

inspections.sort()
print(inspections[-1] * inspections[-2])
