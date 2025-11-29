import numpy as np
import sys
input = sys.stdin.readline

def f1():
    v1, v2 = map(int, input().split())
    v3 = np.array([int(i) for v4 in input().split()])
    v5 = 998244353
    v6 = np.zeros(v2 + 1, dtype='int32')
    v6[0] = 1
    for v4 in range(v1):
        v7 = v6 * 2 % v5
        v7 %= v5
        v7[v3[v4]:] += v6[:-v3[v4]]
        v6 = v7 % v5
    print(v6[v2])
if __name__ == '__main__':
    f1()
