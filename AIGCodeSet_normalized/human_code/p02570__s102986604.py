import sys, math
from collections import defaultdict, deque, Counter
from bisect import bisect_left, bisect_right
from itertools import combinations, permutations, product
from heapq import heappush, heappop
from functools import lru_cache
input = sys.stdin.readline
v1 = lambda: input().strip()
v2 = lambda: int(input())
v3 = lambda: list(map(int, input().split()))
v4 = lambda x, y, v: [[v] * y for v5 in range(x)]
v6 = lambda x, y, z, v: [v4(y, z, v) for v5 in range(x)]
v7 = 1000000007
sys.setrecursionlimit(1000000)
v8, v9, v10 = v3()
if v8 <= v10 * v9:
    print('Yes')
else:
    print('No')
