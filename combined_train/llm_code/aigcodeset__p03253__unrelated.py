import sys
from collections import Counter
from math import sqrt
v1 = 10 ** 9 + 7

def f1(a1):
    v1 = []
    for v2 in range(1, int(sqrt(a1)) + 1):
        if a1 % v2 == 0:
            v1.append(v2)
            if v2 != a1 // v2:
                v1.append(a1 // v2)
    return sorted(v1)

def f2(a1, a2):
    v1 = f1(a2)
    v2 = Counter(v1)
    v3 = [0] * (a1 + 1)
    v3[0] = 1
    for v4, v5 in v2.items():
        for v6 in range(a1, -1, -1):
            for v7 in range(1, min(v6, v5) + 1):
                v3[v6] = (v3[v6] + v3[v6 - v7]) % v1
    return v3[a1]
v2, v3 = map(int, sys.stdin.readline().split())
print(f2(v2, v3))
