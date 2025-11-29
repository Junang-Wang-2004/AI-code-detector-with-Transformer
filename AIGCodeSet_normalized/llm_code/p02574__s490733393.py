import sys
sys.setrecursionlimit(1 << 25)
v1 = sys.stdin.buffer.readline
v2 = sys.stdin.readline
v3 = range
v4 = enumerate

def f1(*a1, **a2):
    print(*a1, **a2)
    sys.exit()

def f2(*a1, a2=1):
    return list(map(lambda x: x - a2, a1))

def f3():
    return int(v1())

def f4():
    return list(map(int, v1().split()))

def f5(a1: int):
    v1 = [a1 + 114514] * (a1 + 1)
    v1[0] = 0
    v1[1] = 1
    for v2 in range(2, int(a1 ** 0.5) + 1):
        if v1[v2] == a1 + 114514:
            for v3 in range(v2, a1 + 1, v2):
                v1[v3] = min(v1[v3], v2)
    return v1
v5 = f5(10 ** 6)
from collections import Counter

def f6(a1: int):
    if a1 == 1:
        return []
    v1 = []
    v2 = a1
    while v2 != 1:
        v3 = v5[v2]
        v2 //= v3
        v1.append(v3)
    return Counter(v1)
v6 = 10 ** 9 + 7
v7 = 2 ** 31
from collections import defaultdict, Counter, deque
from math import gcd
v8 = f3()
v9 = f4()
v10 = 0
v11 = defaultdict(lambda: 0)
v12 = 1
for v13 in v9:
    v10 = gcd(v10, v13)
    if v12:
        for v14, v15 in f6(v13).items():
            if v11[v14] != 0:
                v12 = 0
            v11[v14] += v15
if v10 > 1:
    print('not coprime')
elif v12:
    print('pairwise coprime')
else:
    print('setwise coprime')
