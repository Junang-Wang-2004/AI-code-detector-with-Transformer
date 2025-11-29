import sys
v1 = sys.stdin.buffer.read
input = sys.stdin.buffer.readline
v2 = sys.stdin.buffer.readlines
import numpy as np

def f1():
    v1 = np.array(v1().split(), np.int64)
    v2 = v1[0]
    v3 = v1[1]
    v4 = v1[2:]
    v5, v6 = np.split(v4, 2)
    v5.sort()
    v6.sort()
    v6 = v6[::-1]
    v7 = 0
    v8 = 10 ** 12 + 1
    v9 = sum(v5)
    while v8 - v7 > 1:
        v10 = (v8 + v7) // 2
        if v9 - np.minimum(v5, v10 // v6).sum() <= v3:
            v8 = v10
        else:
            v7 = v10
    print(v8 if v9 - v3 > 0 else 0)
if __name__ == '__main__':
    f1()
