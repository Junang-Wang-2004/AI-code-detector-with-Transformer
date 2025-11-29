import bisect
import collections
import copy
import functools
import heapq
import math
import sys
from collections import deque
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
v1 = 10 ** 9 + 7
v2 = int(input())
v3 = [int(input()) for v4 in range(v2)]
v5 = deque([v3[0]])
for v6 in range(1, len(v3)):
    if v3[v6] <= v5[0]:
        v5.appendleft(v3[v6])
    else:
        v5[bisect.bisect_left(v5, v3[v6]) - 1] = v3[v6]
print(len(v5))
