import sys
import math
from bisect import bisect_right as br
from bisect import bisect_left as bl
sys.setrecursionlimit(1000000000)
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
v3 = f1()
v4 = f2()
v5, v6 = (max(v4), min(v4))
v7, v8 = (v4.index(v5), v4.index(v6))
for v9 in range(v3 - 1):
    if v4[v9] > v4[v9 + 1]:
        break
else:
    print(0)
    quit()
for v9 in range(v3):
    if v4[v9] < 0:
        break
else:
    print(v3 - 1)
    for v9 in range(v3 - 1):
        print(v9 + 1, v9 + 2)
    quit()
for v9 in range(v3):
    if v4[v9] > 0:
        break
else:
    print(v3 - 1)
    for v9 in range(v3 - 1)[::-1]:
        print(v9 + 2, v9 + 1)
    quit()
if abs(v5) >= abs(v6):
    print((v3 - 1) * 2)
    for v9 in range(v3):
        if v9 == v7:
            continue
        print(v7 + 1, v9 + 1)
    for v9 in range(v3 - 1):
        print(v9 + 1, v9 + 2)
else:
    print((v3 - 1) * 2)
    for v9 in range(v3):
        if v9 == v8:
            continue
        print(v8 + 1, v9 + 1)
    for v9 in range(v3 - 1)[::-1]:
        print(v9 + 2, v9 + 1)
