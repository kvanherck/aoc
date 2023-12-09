#!/usr/bin/env python3
import sys
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view
sys.path.append('..')
from common import *

a = np.asarray(list(inputInts()))
v = sliding_window_view(a, 3).transpose()
s = sum(v)
d = s[1:] - s[:-1]
n = sum(d > 0)

print(n)
