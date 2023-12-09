#!/usr/bin/env python3
import sys
sys.path.append('..')
from intcode import cpu

cpu.load()
cpu.run()
print(cpu.mem[0])
