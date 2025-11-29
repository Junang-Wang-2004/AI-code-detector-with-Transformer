import sys
from collections import defaultdict
v1 = 10 ** 9 + 7

def f1(a1, a2, a3, a4):
    if a4[a1] != -1:
        return a4[a1]
    v1 = [1] * K
    for v2 in a3[a1]:
        if v2 == a2:
            continue
        v3 = f1(v2, a1, a3, a4)
        for v4 in range(K):
            v1[v4] = v1[v4] * (K - 1 - sum((v3[j] for v5 in range(K) if v5 != v4))) % v1
    a4[a1] = v1
    return v1

def f2(a1, a2, a3):
    v1 = defaultdict(list)
    for v2, v3 in a3:
        v1[v2].append(v3)
        v1[v3].append(v2)
    v4 = [-1] * (a1 + 1)
    v5 = f1(1, 0, v1, v4)
    return sum(v5) % v1

def f3():
    v1, v2 = map(int, sys.stdin.readline().split())
    v3 = [tuple(map(int, sys.stdin.readline().split())) for v4 in range(v1 - 1)]
    print(f2(v1, v2, v3))
if __name__ == '__main__':
    f3()
