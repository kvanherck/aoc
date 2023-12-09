#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

mem = {}
maskAnd = 0
maskOr = 0
allones = (1 << 36) - 1

for line in inputLines():
	print(line)
	if line.startswith('mask = '):
		m = line[7:]
		assert len(m) == 36
		mm = m.replace('0', '1').replace('X', '0')
		maskAnd = int(mm, 2) ^ allones
		mm = m.replace('X', '0')
		maskOr = int(mm, 2)
		print(bin(maskAnd))
		print(bin(maskOr))
	elif line.startswith('mem'):
		addr, value = re.match(r'mem\[(\d+)\] = (\d+)', line).groups()
		addr = int(addr)
		value = int(value)
		value &= maskAnd
		value |= maskOr
		mem[addr] = value
		print(addr, value)

print(sum(list(mem.values())))
