#!/usr/bin/env python3
import sys
sys.path.append('..')
from intcode import cpu

for a in range(100):
    for b in range(100):
        cpu.load()
        cpu.mem[1] = a
        cpu.mem[2] = b
        cpu.run()
        if cpu.mem[0] == 19690720:
            print(a, b)
            sys.exit(0)
