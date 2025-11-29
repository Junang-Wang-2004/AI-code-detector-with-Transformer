from collections import defaultdict, deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random

def f1():
    return [int(x) for v1 in sys.stdin.readline().split()]

def f2():
    return int(sys.stdin.readline())

def f3():
    return [list(x) for v1 in sys.stdin.readline().split()]

def f4():
    return list(sys.stdin.readline())[:-1]

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
    v1 = f2()
    v2 = f1()
    if sum(v2) == 0:
        print('Yes')
        return
    if v1 % 3 != 0:
        print('No')
        return
    v3 = defaultdict(lambda: 0)
    for v4 in v2:
        v3[v4] += 1
    if len(list(v3.items())) == 2:
        if v3[0] == v1 // 3:
            print('Yes')
            return
        else:
            print('No')
            return
    v5 = 0
    for v4, v6 in v3.items():
        v5 ^= v4
        if v6 != v1 // 3:
            print('No')
            return
    if not v5:
        print('Yes')
        return
    print('No')
    return

def f10():
    v1, v2 = f1()
    v3 = []
    v4 = [0] * (v1 + 1)
    for v5 in range(v2):
        v6, v7 = f1()
        v3.append([v6, v7])
        v4[v6] ^= 1
    for v5 in range(v2):
        v6, v7 = v3[v5]
        if v4[v6]:
            v3[v5] = [v7, v6]
            v4[v6] ^= 1
            v4[v7] ^= 1
    if sum(v4):
        print(-1)
    else:
        for v5 in v3:
            print(*v5)
    return

def f11():
    v1 = f2()
    v2 = [1 << i for v3 in range(100)]
    if v1 in v2:
        print('No')
        quit()
    if v1 + 1 in v2:
        print('Yes')
        for v3 in range(1, 2 * v1):
            print(v3, v3 + 1)
        quit()
    v4 = []
    for v3 in range(1, 3):
        v4.append((v3, v3 + 1))
    v4.append((3, v1 + 1))
    for v3 in range(1, 3):
        v4.append((v3 + v1, v3 + v1 + 1))
    v5 = 1
    v6 = 1
    for v3 in range(2, v1 // 2 + v1 % 2):
        v4.append((v5, 2 * v3))
        v4.append((v6, 2 * v3 + 1))
        v4.append((2 * v3, 2 * v3 + v1 + 1))
        v4.append((2 * v3 + 1, 2 * v3 + v1))
        v5 = 2 * v3 + v1 + 1
        v6 = 2 * v3 + v1
    if v1 % 2:
        print('Yes')
        for v3, v7 in v4:
            print(v3, v7)
    else:
        v4.append((v1 - 1, v1))
        for v3 in range(v1):
            if v2[v3] & v1:
                break
        v4.append((v2[v3 + 1] - 2, 2 * v1))
        print('Yes')
        for v3, v7 in v4:
            print(v3, v7)
    return

def f12():
    v1 = f2()
    return

def f13():
    v1 = f2()
    return

def f14():
    v1 = f2()
    return
if __name__ == '__main__':
    f9()
