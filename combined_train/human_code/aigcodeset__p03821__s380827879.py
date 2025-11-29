import sys
import math
import bisect
sys.setrecursionlimit(1000000000)
from heapq import heappush, heappop
from collections import defaultdict
from itertools import accumulate
from collections import Counter
from collections import deque
from operator import itemgetter
from itertools import permutations
v1 = 10 ** 9 + 7
v2 = int(sys.stdin.readline())
v3, v4 = ([], [])
for v5 in range(v2):
    v6, v7 = map(int, sys.stdin.readline().split())
    v3.append(v6)
    v4.append(v7)
v8 = 0
for v9 in range(v2)[::-1]:
    v6 = -(v3[v9] + v8) % v4[v9]
    v8 += v6
print(v8)
