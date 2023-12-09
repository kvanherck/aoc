#!/usr/bin/env python3
import sys
sys.path.append('..')
from intcode import cpu

cpu.load([1002,4,3,4,33])
cpu.run()
assert cpu.mem[4] == 99

cpu.load([1101,100,-1,4,0])
cpu.run()
assert cpu.mem[4] == 99

cpu.load()
cpu.run(input=[1])
