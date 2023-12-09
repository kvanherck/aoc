#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *
import numpy as np

def decode(s):
	print(s)
	b = bin(int(s, 16))[2:].zfill(len(s) * 4)
	decodePacket(b)
	print()

level = 0

def decodePacket(b):
	global level
	indent = '    ' * level
	level += 1
	version = b[:3]
	b = b[3:]
	typ = int(b[:3], 2)
	b = b[3:]
	if typ == 4:
		literal = ''
		while True:
			v = b[:5]
			b = b[5:]
			literal += v[1:]
			if v[0] == '0':
				break
		print(f'{indent}Literal: {literal} = {int(literal, 2)}')
		level -= 1
		return b, int(literal, 2)
	else:
		values = []
		mode = b[0]
		b = b[1:]
		if mode == '0':
			length = int(b[:15], 2)
			b = b[15:]
			print(f'{indent}Operator: length = {length}')
			bb = b[:length]
			b = b[length:]
			while bb:
				bb, x = decodePacket(bb)
				values.append(x)
		else:
			length = int(b[:11], 2)
			b = b[11:]
			print(f'{indent}Operator: subpackets = {length}')
			for i in range(length):
				b, x = decodePacket(b)
				values.append(x)
		if typ == 0:
			result = sum(values)
			print(f'{indent}Sum: {values} = {result}')
		if typ == 1:
			result = 1
			for x in values:
				result *= x
			print(f'{indent}Product: {values} = {result}')
		if typ == 2:
			result = min(values)
			print(f'{indent}Min: {values} = {result}')
		if typ == 3:
			result = max(values)
			print(f'{indent}Max: {values} = {result}')
		if typ == 5:
			result = int(values[0] > values[1])
			print(f'{indent}Greater than: {values} = {result}')
		if typ == 6:
			result = int(values[0] < values[1])
			print(f'{indent}Less than: {values} = {result}')
		if typ == 7:
			result = int(values[0] == values[1])
			print(f'{indent}Equal: {values} = {result}')
		level -= 1
		return b, result

decode('C200B40A82')
decode('04005AC33890')
decode('880086C3E88112')
decode('CE00C43D881120')
decode('D8005AC2A8F0')
decode('F600BC2D8F')
decode('9C005AC2F8F0')
decode('9C0141080250320F1802104A08')

for line in inputLines():
	decode(line)
