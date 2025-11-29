from collections import defaultdict, deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, random, itertools, math
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline
v1 = math.sqrt

def f1():
    return list(map(int, input().split()))

def f2():
    return list(map(float, input().split()))

def f3():
    return list(map(lambda x: int(x) - 1, input().split()))

def f4():
    return int(input())

def f5():
    return float(input())

def f6():
    return input().rstrip()

def f7():
    return f6().split()

def f8(a1):
    return [f4() for v1 in range(a1)]

def f9(a1):
    return [f1() for v1 in range(a1)]

def f10(a1):
    return [f5() for v1 in range(a1)]

def f11(a1):
    return [f1() for v1 in range(a1)]

def f12(a1):
    return [f3() for v1 in range(a1)]

def f13(a1):
    return [f6() for v1 in range(a1)]

def f14(a1):
    return [f7() for v1 in range(a1)]
v2 = 1000000007
v3 = 10000000000.0

def f15():
    v1, v2, v3 = f1()
    v4 = f6()
    v5 = [v3]
    v6 = -v3
    for v7 in range(v1 - 1, -1, -1):
        if v5[-1] - v3 > v7 and v4[v7] == 'o':
            v5.append(v7)
            if len(v5) > v2:
                break
    v5.remove(v3)
    v5.sort()
    if len(v5) != v2:
        return
    v8 = [0] * (v1 + 1)
    for v7 in range(v1):
        if v4[v7] == 'o' and v6 + v3 + 1 <= v7:
            v6 = v7
            v8[v7 + 1] = v8[v7] + 1
        else:
            v8[v7 + 1] = v8[v7]
    v9 = []
    v6 = 0
    for v6, v10 in enumerate(v5):
        if v10 == 0:
            v9.append(str(v10 + 1))
            continue
        if v8[v10] == v6:
            v9.append(str(v10 + 1))
    print('\n'.join(v9))
    return
if __name__ == '__main__':
    f15()
