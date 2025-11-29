import sys
import math
import bisect
from collections import defaultdict, deque, Counter
from heapq import heappush, heappop

def f1():
    return [int(x) for v1 in sys.stdin.readline().split()]

def f2():
    return int(sys.stdin.readline())

def f3():
    v1 = list(sys.stdin.readline())
    if v1[-1] == '\n':
        return v1[:-1]
    return v1

def f4(a1):
    return [f2() for v1 in range(a1)]

def f5():
    v1 = list(map(int, list(input())))
    v2 = f2()
    v3 = len(v1)
    if v2 == 1:
        v4 = v1[0] + 9 * (v3 - 1)
        print(v4)
    elif v2 == 2:
        if v3 < 2:
            print(0)
            return
        v4 = (v3 - 1) * (v3 - 2) * 81 // 2 + v1[0] * 9 * (v3 - 1) + (v1[1] - 1)
        print(v4)
    elif v2 == 3:
        if v3 < 3:
            print(0)
            return
        v4 = (v3 - 1) * (v3 - 2) * (v3 - 3) * 9 ** 3 // 6 + v1[0] * (v3 - 1) * (v3 - 2) * 81 // 2 + (v1[1] - 1) * 9 + (v1[2] - 1)
        print(v4)
    return
if __name__ == '__main__':
    f5()
