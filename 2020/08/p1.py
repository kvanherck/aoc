#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

program = []
for opcode, arg in inputRE(r'(...) ([+-]?\d+)'):
    program.append((opcode, int(arg)))

acc = 0
pc = 0
executed = set()
while True:
    if pc in executed:
        print(f'Infinite loop @ {pc}: acc = {acc}')
        break
    executed.add(pc)
    opcode, arg = program[pc]
    print(f'{pc}: {opcode} {arg}: acc = {acc}')
    if opcode == 'nop':
        pc += 1
    elif opcode == 'acc':
        pc += 1
        acc += arg
    elif opcode == 'jmp':
        pc += arg

print(acc)
