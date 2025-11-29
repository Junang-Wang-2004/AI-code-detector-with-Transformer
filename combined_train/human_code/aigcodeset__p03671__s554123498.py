import sys
import math
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from copy import deepcopy
from fractions import gcd
from functools import lru_cache, reduce
from heapq import heappop, heappush
from itertools import accumulate, groupby, product, permutations, combinations, combinations_with_replacement
from math import ceil, floor, factorial, log, sqrt, sin, cos
from operator import itemgetter
from string import ascii_lowercase, ascii_uppercase, digits
sys.setrecursionlimit(10 ** 7)
v1 = lambda: sys.stdin.readline().rstrip()
v2 = lambda: int(v1())
v3 = lambda: float(v1())
v4 = lambda: [_ for v5 in v1().split()]
v6 = lambda: [int(v5) for v5 in v1().split()]
v7 = lambda: [float(v5) for v5 in v1().split()]
v8 = float('inf')
v9 = 10 ** 9 + 7
print(sum(sorted(v6())[:2]))
