import sys
from typing import List
v1 = sys.stdin.readline
v2 = sys.stdout.write

def f1():
    v1 = 10 ** 9 + 7
    v2, v3, v4 = map(int, v1().split())

    def comb(a1: int, a2: int) -> int:
        if a1 < a2:
            return 0
        return fact[a1] * factinv[a2] * factinv[a1 - a2] % v1
    v5 = [1]
    v6 = [1]
    v7 = [0, 1]
    for v8 in range(2, v2 * v3 + 1):
        v5.append(v5[-1] * v8 % v1)
        v7.append((v1 - v7[v1 % v8] * (v1 // v8)) % v1)
        v6.append(v6[-1] * v7[-1] % v1)
    v9 = 0
    for v8 in range(1, v4 + 1):
        v9 += comb(v2 * v3, v8) * (2 * v8 * (v2 + v3 - 2) * (v2 * v3 - v8) % v1)
        v9 %= v1
    v2('%d\n' % v9)
f1()
