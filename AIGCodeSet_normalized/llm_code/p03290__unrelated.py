import sys
from typing import List

def f1(a1: int, a2: int, a3: List[int], a4: List[int]) -> int:
    v1 = sum(a3)
    v2 = [0] * (v1 + 1)
    for v3 in range(1, a1 + 1):
        for v4 in range(v1, -1, -1):
            for v5 in range(1, min(v4, a3[v3 - 1]) + 1):
                v2[v4] = max(v2[v4], v2[v4 - v5] + v5 * 100 * v3 + (a4[v3 - 1] if v5 == a3[v3 - 1] else 0))
    for v3 in range(v1 + 1):
        if v2[v3] >= a2:
            return v3
    return -1

def f2():
    v1, v2 = map(int, sys.stdin.readline().split())
    v3 = []
    v4 = []
    for v5 in range(v1):
        v6, v7 = map(int, sys.stdin.readline().split())
        v3.append(v6)
        v4.append(v7)
    print(f1(v1, v2, v3, v4))
if __name__ == '__main__':
    f2()
