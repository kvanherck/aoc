#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

mem = {}
mask = None
maskAnd = 0
maskOr = 0
allones = (1 << 36) - 1

def writeWithMask(addr, value, mask):
	if 'X' in mask:
		pos = mask.find('X')
		newMask = mask[:pos] + '0' + mask[pos+1:]
		writeWithMask(addr, value, newMask)
		newMask = mask[:pos] + '1' + mask[pos+1:]
		writeWithMask(addr, value, newMask)
	else:
		addr |= int(mask, 2)
		mem[addr] = value
		# print(bin(addr), value)

for line in inputLines():
	print(line)
	if line.startswith('mask = '):
		m = line[7:]
		assert len(m) == 36
		mask = m
		mm = m.replace('X', '1')
		maskAnd = int(mm, 2) ^ allones
	elif line.startswith('mem'):
		addr, value = re.match(r'mem\[(\d+)\] = (\d+)', line).groups()
		addr = int(addr)
		addr &= maskAnd
		value = int(value)
		writeWithMask(addr, value, mask)

print(sum(list(mem.values())))
