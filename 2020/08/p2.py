#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

program = []
for opcode, arg in inputRE(r'(...) ([+-]?\d+)'):
    program.append((opcode, int(arg)))

def execute(program):
    acc = 0
    pc = 0
    executed = set()
    while True:
        if pc in executed:
            print(f'Infinite loop @ {pc}: acc = {acc}')
            return None
        if pc == len(program):
            print(f'Program finished @ {pc}')
            return acc
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

for i in range(len(program)):
    new = program[:]
    opcode, arg = new[i]
    if opcode == 'nop':
        print(f'{i}: nop -> jmp')
        new[i] = ('jmp', arg)
    elif opcode == 'jmp':
        print(f'{i}: jmp -> nop')
        new[i] = ('nop', arg)

    if new != program:
        acc = execute(new)
        print()
        if acc is not None:
            print(acc)
            break
