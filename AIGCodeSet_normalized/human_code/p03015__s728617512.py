from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations, accumulate
import sys
import math
import bisect

def f1():
    return [int(x) for v1 in sys.stdin.readline().split()]

def f2():
    return int(sys.stdin.readline())

def f3():
    return [list(x) for v1 in sys.stdin.readline().split()]

def f4():
    v1 = list(sys.stdin.readline())
    if v1[-1] == '\n':
        return v1[:-1]
    return v1

def f5(a1):
    return [f2() for v1 in range(a1)]

def f6(a1):
    return [f1() for v1 in range(a1)]

def f7(a1):
    return [f4() for v1 in range(a1)]

def f8(a1):
    return [f3() for v1 in range(a1)]
sys.setrecursionlimit(1000000)
v1 = 1000000007

def f9():
    v1 = list(map(int, input()))
    v2 = len(v1)
    v3 = [[0] * 2 for v4 in range(v2 + 1)]
    v3[0][0] = 1
    for v4 in range(v2):
        v5 = v4 + 1
        for v6 in range(2):
            v7 = 1 if v6 else v1[v4]
            for v8 in range(v7 + 1):
                v9 = v6 or v8 < v1[v4]
                if v8:
                    v3[v5][v9] += 2 * v3[v4][v6]
                else:
                    v3[v5][v9] += v3[v4][v6]
                v3[v5][v9] %= v1
    print(sum(v3[v2]) % v1)
    return
if __name__ == '__main__':
    f9()
