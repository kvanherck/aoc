#!/usr/bin/env python3
import struct
from cpu import CPU

INPUT_FILE = 'challenge.bin'

walkthrough = """take tablet
use tablet
doorway
north
north
bridge
continue
down
east
take empty lantern
west
west
passage
ladder
west
south
north
take can
use can
use lantern
west
ladder
darkness
continue
west
west
west
west
north
take red coin
look red coin
north
east
take concave coin
look concave coin
down
take corroded coin
look corroded coin
up
west
west
take blue coin
look blue coin
up
take shiny coin
look shiny coin
down
east
use blue coin
use red coin
use shiny coin
use concave coin
use corroded coin
north
take teleporter
use teleporter
north
north
north
north
north
north
north
east
take journal
west
north
north
take orb
north
east
east
north
west
south
east
east
west
north
north
east
vault
take mirror
use mirror
"""

def load(fileName=INPUT_FILE):
    program = []
    with open(fileName, 'rb') as f:
        while True:
            data = f.read(2)
            if not data:
                break
            x = struct.unpack('<H', data)
            program.append(x[0])
    return program

def main():
    program = load()
    print(f'Loaded program of {len(program)} instructions')
    cpu = CPU()
    cpu.load(program)
    cpu.mem[5451] = 21
    cpu.mem[5452] = 21
    cpu.mem[5453] = 21
    cpu.mem[5489] = 21
    cpu.mem[5490] = 21
    cpu.mem[5485] = 6
    cpu.mem[5487] = 0x8000 + 7
    cpu.mem[5488] = 25734
    print('Teleport algorithm: r0 = f(r0, r1, r7)')
    cpu.disassemble(6027, 40)
    print()
    print('Hacked teleport')
    cpu.disassemble(5451, 47)
    cpu.run(walkthrough, verbose=False)

if __name__ == '__main__':
    main()
