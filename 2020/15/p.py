#!/usr/bin/env python3
import sys
import time

# inputs = [0, 3, 6]
# inputs = [1, 3, 2]
# inputs = [3, 1, 2]
inputs = [0, 14, 6, 20, 1, 4]

def main():
    d = {}
    m = None
    for i, n in enumerate(inputs):
        # print(i+1, n)
        if m is not None:
            d[m] = j
        m = n
        j = i

    t1 = s = time.time()
    i += 1
    while i < 30000000:
        t2 = time.time()
        if t2 - t1 > 1:
            print(f'... working for {t2 - s:.1f} seconds @ {i}')
            t1 = t2
        if m in d:
            k = d[m]
            n = j - k
            # print(m, k, n)
        else:
            n = 0
            # print(m, -1, n)
        d[m] = j
        m = n
        j = i
        # print(i+1, n)
        i += 1
        if i == 2020:
            print(i, n)
    print(i, n)


if __name__ == '__main__':
    main()
