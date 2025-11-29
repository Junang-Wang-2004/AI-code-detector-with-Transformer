import sys
import numpy as np
v1 = np.array(sys.stdin.read().split(), dtype=np.int64)
v2 = v1[1:]

def f1():
    v1 = np.bincount(v2)
    v2 = np.count_nonzero(v1)
    v1 = np.maximum(0, v1 - 1)
    v2 -= np.sum(v1) & 1
    return v2
if __name__ == '__main__':
    v3 = f1()
    print(v3)
