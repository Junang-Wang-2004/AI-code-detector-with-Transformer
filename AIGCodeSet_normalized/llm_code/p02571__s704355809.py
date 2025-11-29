import sys
import math
from collections import deque
sys.setrecursionlimit(1000000)
v1 = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
v2 = lambda: int(input())
v3 = lambda: map(int, input().split())
v4 = lambda: list(v3())
v5 = lambda: input()

def f1(a1, a2, a3):
    return [[int(a3)] * a2 for v1 in range(a1)]

def f2():
    v1 = v5()
    v2 = v5()
    v3, v4 = (len(v1), len(v2))
    v5 = v4
    for v6 in range(v3 - v4 + 1):
        v7 = 0
        v8 = v1[v6:v6 + v4]
        for v9, v10 in zip(v8, v2):
            if v9 != v10:
                v7 += 1
        v5 = min(v5, v7)
    print(v5)
if __name__ == '__main__':
    f2()
