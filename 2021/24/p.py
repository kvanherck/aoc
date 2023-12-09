#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

# part 1: 91297395919993: 76s
# part 2: 71131151917891: 76s

def check(program, inputs):
    regs = {
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0,
    }
    pc = 0
    while pc < len(program):
        line = program[pc]
        pc += 1
        fields = line.split()
        if fields[0] == 'inp':
            assert fields[1] == 'w'
            w = inputs.pop(0)
            regs['w'] = w
        else:
            opcode = fields[0]
            a = regs[fields[1]]
            if fields[2] in ('w', 'x', 'y', 'z'):
                b = regs[fields[2]]
            else:
                b = int(fields[2])
            if opcode == 'add':
                u = a + b
            elif opcode == 'mul':
                u = a * b
            elif opcode == 'div':
                u = a // b
            elif opcode == 'mod':
                u = a % b
            elif opcode == 'eql':
                u = int(a == b)
            regs[fields[1]] = u
    return regs['z'] == 0

def bfs_run(program, pc, regs):
    while pc < len(program):
        line = program[pc]
        pc += 1
        fields = line.split()
        if fields[0] == 'inp':
            return regs['z']
        else:
            opcode = fields[0]
            a = regs[fields[1]]
            if fields[2] in ('w', 'x', 'y', 'z'):
                b = regs[fields[2]]
            else:
                b = int(fields[2])
            if opcode == 'add':
                u = a + b
            elif opcode == 'mul':
                u = a * b
            elif opcode == 'div':
                u = a // b
            elif opcode == 'mod':
                u = a % b
            elif opcode == 'eql':
                u = int(a == b)
            regs[fields[1]] = u
    return regs['z']

def bfs_step(program, pc, states_in, w_in):
    states_out = {}
    for w in w_in:
        for z_in in states_in:
            regs = {
                'w': w,
                'x': 0,
                'y': 0,
                'z': z_in,
            }
            z_out = bfs_run(program, pc, regs)
            if z_out < 26**5 and z_out not in states_out:
                states_out[z_out] = states_in[z_in] + [w]
    return states_out

def bfs(program, w_in):
    states = {0: []}
    for pc, line in enumerate(program):
        if line.startswith('inp'):
            states = bfs_step(program, pc + 1, states, w_in)
            print(len(states))
    return states

program = list(inputLines())

start = timer()
states = bfs(program, range(9, 0, -1))
print(''.join(map(str, states[0])))
print(timer() - start)
print(check(program, states[0]))

start = timer()
states = bfs(program, range(1, 10))
print(''.join(map(str, states[0])))
print(timer() - start)
print(check(program, states[0]))
