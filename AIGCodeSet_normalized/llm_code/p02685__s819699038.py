import sys
import math
from bisect import bisect_right as br
from bisect import bisect_left as bl
sys.setrecursionlimit(2147483647)
from heapq import heappush, heappop, heappushpop
from collections import defaultdict
from itertools import accumulate
from collections import Counter
from collections import deque
from operator import itemgetter
from itertools import permutations
v1 = 998244353
v2 = float('inf')

def f1():
    return int(sys.stdin.readline())

def f2():
    return list(map(int, sys.stdin.readline().split()))

def f3(a1, a2):
    return fact[a1] * pow(fact[a1 - a2], v1 - 2, v1) * pow(fact[a2], v1 - 2, v1) % v1
v3, v4, v5 = f2()
v6 = [1] * (v4 + 1)
for v7 in range(1, v4 + 1):
    v6[v7] = v6[v7 - 1] * v7
    v6[v7] %= v1
v8 = 0
for v7 in range(v5 + 1):
    v8 += f3(v3 - 1, v7) * v4 * pow(v4 - 1, v3 - 1 - v7, v1)
    v8 %= v1
print(v8)
