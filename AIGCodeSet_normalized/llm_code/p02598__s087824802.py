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
v1 = 10 ** 9 + 7
v2 = float('inf')

def f1():
    return int(sys.stdin.readline())

def f2():
    return list(map(int, sys.stdin.readline().split()))

def f3(a1):
    v1 = k
    for v2 in a:
        v3 = math.ceil(v2 / a1)
        v1 -= v3 - 1
        if v1 < 0:
            return False
    return True
v3, v4 = f2()
v5 = f2()
v5.sort(reverse=True)
v6 = sum(v5)
v7 = 0
while v6 - v7 > 1:
    v8 = (v6 + v7) // 2
    if f3(v8):
        v6 = v8
    else:
        v7 = v8
print(v6)
