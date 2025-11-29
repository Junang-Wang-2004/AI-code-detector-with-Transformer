import sys
from heapq import heappop, heappush
from operator import itemgetter
from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
v1 = 10 ** 9 + 7
v2 = float('inf')

def f1():
    v1, v2 = map(int, input().split())
    v3 = list(map(int, input().split()))
    v4 = list(map(int, input().split()))
    v3.sort()
    v4.sort(reverse=True)

    def isOk(a1):
        v1 = 0
        for v2, v3 in zip(v3, v4):
            v4 = a1 // v3
            if v2 <= v4:
                continue
            v1 += v2 - v4
        if v1 > v2:
            return False
        else:
            return True
    v5 = -1
    v6 = v3[-1] * v4[0]
    while v6 - v5 > 1:
        v7 = (v6 + v5) // 2
        if isOk(v7):
            v6 = v7
        else:
            v5 = v7
    print(v6)
f1()
