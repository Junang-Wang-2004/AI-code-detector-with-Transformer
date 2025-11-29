import math
import itertools
import queue
import bisect
from collections import deque, defaultdict
import heapq as hpq
from sys import stdin, setrecursionlimit
v1 = stdin.readline
setrecursionlimit(10 ** 7)

def f1():
    v1 = int(v1())
    v2 = [int(v1()) for v3 in range(v1)]
    v2.sort()
    if v1 % 2:
        v4 = v2[v1 // 2 + 1] - v2[v1 // 2 - 1]
        for v3 in range(v1 // 2 - 1):
            v4 += (v2[v1 - 1 - v3] - v2[v3]) * 2
        print(v4 + max(v2[v1 // 2 + 1] - v2[v1 // 2], v2[v1 // 2] - v2[v1 // 2 - 1]))
    else:
        v4 = v2[v1 // 2] - v2[v1 // 2 - 1]
        for v3 in range(v1 // 2 - 1):
            v4 += (v2[v1 - 1 - v3] - v2[v3]) * 2
        print(v4)
    return None
if __name__ == '__main__':
    f1()
