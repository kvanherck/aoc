#!/usr/bin/env python3
import sys
sys.path.append('..')
from common import *

energies = []
for chunk in inputChunks():
    energy = sum([int(line) for line in chunk])
    energies.append(energy)

energies.sort()
energies.reverse()
print(energies[:3])
print(sum(energies[:3]))
