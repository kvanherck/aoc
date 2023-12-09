#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *
import numpy as np

def decode(s):
	print(s)
	versionSum = 0
	x = int(s, 16)
	l = len(s) * 4
	b = f'{x:b}'
	if len(b) < l:
		b = '0' * (l - len(b)) + b
	while len(b) >= 6:
		# print(b)
		version = b[:3]
		print(f'Version: {int(version, 2)}')
		# if version == '000':
		# 	break
		versionSum += int(version, 2)
		b = b[3:]
		typ = b[:3]
		b = b[3:]
		if typ == '100':
			literal = ''
			while True:
				v = b[:5]
				b = b[5:]
				literal += v[1:]
				if v[0] == '0':
					break
			print(f'Literal: {literal} = {int(literal, 2)}')
		else:
			if len(b) < 1:
				break
			mode = b[0]
			b = b[1:]
			if mode == '0':
				if len(b) < 15:
					break
				length = int(b[:15], 2)
				b = b[15:]
				print(f'Operator: length = {length}')
			else:
				if len(b) < 11:
					break
				length = int(b[:11], 2)
				b = b[11:]
				print(f'Operator: subpackets = {length}')
	print(f'Version sum: {versionSum}')
	return versionSum

decode('D2FE28')
decode('38006F45291200')
decode('EE00D40C823060')
decode('8A004A801A8002F478')
decode('620080001611562C8802118E34')
decode('C0015000016115A2E0802F182340')
decode('A0016C880162017C3686B18A3D4780')

print()

for line in inputLines():
	decode(line)
