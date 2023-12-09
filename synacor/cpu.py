#!/usr/bin/env python3
import sys
import code

class CPU:
    def __init__(self):
        self.instructions = {
            0: (self.halt, 0, 0),
            1: (self.set, 1, 1),
            2: (self.push, 1, 0),
            3: (self.pop, 0, 1),
            4: (self.eq, 2, 1),
            5: (self.gt, 2, 1),
            6: (self.jmp, 1, 0),
            7: (self.jt, 2, 0),
            8: (self.jf, 2, 0),
            9: (self.add, 2, 1),
            10: (self.mult, 2, 1),
            11: (self.mod, 2, 1),
            12: (self.and_, 2, 1),
            13: (self.or_, 2, 1),
            14: (self.not_, 1, 1),
            15: (self.rmem, 1, 1),
            16: (self.wmem, 2, 0),
            17: (self.call, 1, 0),
            18: (self.ret, 0, 0),
            19: (self.out, 1, 0),
            20: (self.in_, 0, 1),
            21: (self.nop, 0, 0),
        }

    def load(self, program):
        self.mem = program

    def disassemble(self, address, n=1):
        a = address
        while a < address + n:
            opcode = self.mem[a]
            fn, nin, nout = self.instructions[opcode]
            instr = fn.__name__
            if instr.endswith('_'):
                instr = instr[:-1]
            args = []
            if nout == 1:
                x = self.mem[a + 1]
                if x <= 0x7fff:
                    args.append(str(x))
                else:
                    args.append(f'r{x - 0x8000}')
            for i in range(nin):
                x = self.mem[a + 1 + nout + i]
                if x <= 0x7fff:
                    if instr == 'out':
                        args.append(f"'{chr(x)}'")
                    else:
                        args.append(str(x))
                else:
                    args.append(f'r{x - 0x8000}')
            arglist = ', '.join(args)
            print(f'{a:3d}: {instr} {arglist}')
            a += 1 + nout + nin

    def run(self, input=None, pc=0, verbose=True, breakpoints=[]):
        self.input = input
        self.verbose = verbose
        self.trace = False
        self.output = []
        self.pc = pc
        self.running = True
        self.regs = [0] * 8
        self.stack = []
        self.breakpoints = breakpoints
        while self.running:
            if self.trace:
                self.disassemble(self.pc)
            if self.pc in self.breakpoints:
                break
            opcode = self.mem[self.pc]
            if opcode not in self.instructions:
                raise RuntimeError(f'Unknown instruction: {opcode}')
            fn, nin, nout = self.instructions[opcode]
            if nout == 1:
                dest = self.mem[self.pc + 1]
            inputs = []
            for i in range(nin):
                x = self.mem[self.pc + 1 + nout + i]
                if x <= 0x7fff:
                    inputs.append(x)
                elif x <= 0x8007:
                    inputs.append(self.regs[x - 0x8000])
                else:
                    raise RuntimeError(f'Invalid input: {x}')
            self.pc += 1 + nin + nout
            u = fn(*inputs)
            if nout:
                if dest <= 0x7fff:
                    self.mem[dest] = u
                elif dest <= 0x8007:
                    self.regs[dest - 0x8000] = u
                else:
                    raise RuntimeError(f'Invalid output: {dest}')
        return self.output

    def halt(self):
        self.running = False

    def set(self, b):
        return b

    def push(self, a):
        self.stack.append(a)

    def pop(self):
        return self.stack.pop()

    def eq(self, b, c):
        return int(b == c)

    def gt(self, b, c):
        return int(b > c)

    def jmp(self, a):
        self.pc = a

    def jt(self, a, b):
        if a:
            self.pc = b

    def jf(self, a, b):
        if not a:
            self.pc = b

    def add(self, b, c):
        return (b + c) % 0x8000

    def mult(self, b, c):
        return (b * c) % 0x8000

    def mod(self, b, c):
        return b % c

    def and_(self, b, c):
        return b & c

    def or_(self, b, c):
        return b | c

    def not_(self, b):
        return b ^ 0x7fff

    def rmem(self, a):
        return self.mem[a]

    def wmem(self, a, b):
        self.mem[a] = b

    def call(self, a):
        self.stack.append(self.pc)
        self.pc = a

    def ret(self):
        self.pc = self.stack.pop()

    def out(self, a):
        if self.verbose:
            sys.stdout.write(chr(a))
        self.output.append(a)

    def in_(self):
        if self.input:
            c = self.input[0]
            self.input = self.input[1:]
        else:
            if not self.verbose:
                self.verbose = True
                print('Preloaded input exhausted, enabling interactive input.\nUse Ctrl-Z to stop or Ctrl-C to debug.')
            while True:
                try:
                    c = sys.stdin.read(1)
                    break
                except KeyboardInterrupt:
                    print('Enabling interactive console, type Ctrl-Z to continue, exit() to stop.')
                    def exit():
                        raise SystemExit()
                    code.interact(local=locals())
        if c:
            return ord(c)
        else:
            self.running = False
            return 0

    def nop(self):
        pass
