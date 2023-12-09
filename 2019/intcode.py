#!/usr/bin/env python3
import sys
from collections import defaultdict

DEFAULT_INPUT = 'input.txt'

class CPU:
    MODE_POSITION = 0
    MODE_IMMEDIATE = 1

    def __init__(self):
        self.instructions = {
            1: (self.add, 2, 1),
            2: (self.mul, 2, 1),
            3: (self.input, 0, 1),
            4: (self.output, 1, 0),
            5: (self.jnz, 2, 0),
            6: (self.jz, 2, 0),
            7: (self.lt, 2, 1),
            8: (self.eq, 2, 1),
            99: (self.stop, 0, 0),
        }

    def load(self, program=None):
        if program:
            self.mem = program
        else:
            if len(sys.argv) == 1:
                inputFile = DEFAULT_INPUT
            elif len(sys.argv) == 2:
                inputFile = sys.argv[1]
            else:
                sys.exit(f'Usage: {sys.argv[0]} [{DEFAULT_INPUT}]')
            with open(inputFile) as f:
                line = f.read()
            self.mem = [int(x) for x in line.split(',')]

    def disassemble(self):
        Disassembler().disassemble(self.mem)

    def run(self, input=None, verbose=True):
        self.input = input
        self.verbose = verbose
        self.output = []
        self.pc = 0
        self.running = True
        while self.running:
            instr = self.mem[self.pc]
            opcode = instr % 100
            modes = instr // 100
            assert opcode in self.instructions
            fn, nin, nout = self.instructions[opcode]
            inputs = []
            for i in range(nin):
                x = self.mem[self.pc + 1 + i]
                if modes % 10 == self.MODE_POSITION:
                    x = self.mem[x]
                else:
                    assert modes % 10 == self.MODE_IMMEDIATE
                inputs.append(x)
                modes = modes // 10
            assert modes == 0
            if nout == 1:
                dest = self.mem[self.pc + 1 + nin]
            self.pc += 1 + nin + nout
            u = fn(*inputs)
            if nout == 1:
                self.mem[dest] = u
        return self.output

    def add(self, x, y):
        return x + y

    def mul(self, x, y):
        return x * y

    def input(self):
        if self.input is not None:
            return self.input.pop(0)
        else:
            return int(input('< '))

    def output(self, x):
        if self.verbose:
            print(f'> {x}')
        self.output.append(x)

    def stop(self):
        self.running = False

    def jnz(self, x, y):
        if x:
            self.pc = y

    def jz(self, x, y):
        if not x:
            self.pc = y

    def lt(self, x, y):
        return int(x < y)

    def eq(self, x, y):
        return int(x == y)


class Disassembler:
    MODE_POSITION = 0
    MODE_IMMEDIATE = 1

    def __init__(self):
        self.instructions = {
            1: ('ADD', 2, 1),
            2: ('MUL', 2, 1),
            3: ('IN', 0, 1),
            4: ('OUT', 1, 0),
            5: ('JNZ', 2, 0),
            6: ('JZ', 2, 0),
            7: ('SLT', 2, 1),
            8: ('SEQ', 2, 1),
            99: ('HALT', 0, 0),
        }

    def disassemble(self, program):
        pc = 0
        while pc < len(program):
            try:
                instr = program[pc]
                opcode = instr % 100
                modes = instr // 100
                name, nin, nout = self.instructions[opcode]
                inputs = []
                for i in range(nin):
                    x = program[pc + 1 + i]
                    if modes % 10 == self.MODE_POSITION:
                        x = f'@{x}'
                    else:
                        assert modes % 10 == self.MODE_IMMEDIATE
                        x = f'#{x}'
                    inputs.append(x)
                    modes = modes // 10
                if nout == 1:
                    dest = program[pc + 1 + nin]
                    output = f'@{dest}'
                inputs = ','.join(inputs)
                if nout == 1:
                    if inputs:
                        print(f'{pc:3}: {name} {output},{inputs}')
                    else:
                        print(f'{pc:3}: {name} {output}')
                else:
                    print(f'{pc:3}: {name} {inputs}')
                pc += 1 + nin + nout
            except KeyError:
                print(f'{pc:3}: {instr}')
                pc += 1

cpu = CPU()
