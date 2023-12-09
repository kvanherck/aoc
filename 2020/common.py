#!/usr/bin/env python3
import sys
import re

DEFAULT_INPUT = 'input.txt'

def inputLines(ignoreBlanks=True, stripWhitespace=True):
    if len(sys.argv) == 1:
        inputFile = DEFAULT_INPUT
    elif len(sys.argv) == 2:
        inputFile = sys.argv[1]
    else:
        sys.exit(f'Usage: {sys.argv[0]} [{DEFAULT_INPUT}]')
    n = 0
    with open(inputFile) as f:
        for line in f.readlines():
            if stripWhitespace:
                line = line.strip()
            if ignoreBlanks and not line:
                continue
            yield line
            n += 1
    print(f'Parsed {n} lines')


def inputInts():
    for line in inputLines():
        yield int(line)


def inputRE(pattern):
    r = re.compile(pattern)
    for line in inputLines():
        m = r.match(line)
        yield m.groups()


def inputChunks():
    n = 0
    chunk = []
    for line in inputLines(ignoreBlanks=False):
        if line:
            chunk.append(line)
        else:
            if chunk:
                yield chunk
                n += 1
                chunk = []
    if chunk:
        yield chunk
        n += 1
    print(f'Parsed {n} chunks')


def inputArray(valueMapping={'.': 0, '#': 1}):
    rows = []
    for line in inputLines():
        values = [valueMapping[x] for x in line]
        rows.append(values)
    return rows
