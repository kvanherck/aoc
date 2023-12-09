#!/usr/bin/env python3
import sys
sys.path.append('..')
from intcode import cpu

def run(phases, verbose=True):
	out1 = cpu.run(input=[phases[0], 0], verbose=verbose)
	out2 = cpu.run(input=[phases[1], out1[0]], verbose=verbose)
	out3 = cpu.run(input=[phases[2], out2[0]], verbose=verbose)
	out4 = cpu.run(input=[phases[3], out3[0]], verbose=verbose)
	out5 = cpu.run(input=[phases[4], out4[0]], verbose=verbose)
	return out5[0]

cpu.load([3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0])
cpu.disassemble()
out = run([4, 3, 2, 1, 0])
assert out == 43210

cpu.load([3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0])
cpu.disassemble()
out = run([0, 1, 2, 3, 4])
assert out == 54321

cpu.load([3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0])
cpu.disassemble()
out = run([1, 0, 4, 3, 2])
assert out == 65210

cpu.load()
cpu.disassemble()
mout = 0
mphases = None
for a in range(5):
	for b in range(5):
		if b == a:
			continue
		for c in range(5):
			if c == a or c == b:
				continue
			for d in range(5):
				if d == a or d == b or d == c:
					continue
				for e in range(5):
					if e == a or e == b or e == c or e == d:
						continue
					out = run([a, b, c, d, e], verbose=False)
					if out > mout:
						mout = out
						mphases = (a, b, c, d, e)

print(mphases)
print(mout)

# phase = 0: out = ((in*5+2)*3+2)*4 = in*60 + 32
# phase = 1: out = in*5
# phase = 2: out = (in*2+2)*2 = in*4 + 4
# phase = 3: out = in*4 + 3
# phase = 4: out = ((in*3+5)*3+3)*5 = in*45 + 90

# 4 2 3 0 1
# 90
# 364
# 1459
# 87572
# 437860
