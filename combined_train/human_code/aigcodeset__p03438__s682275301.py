import bisect
import heapq
import itertools
import math
import operator
import os
import re
import string
import sys
from collections import Counter, deque, defaultdict
from copy import deepcopy
from decimal import Decimal
from fractions import gcd
from functools import lru_cache, reduce
from operator import itemgetter, mul, add, xor
import numpy as np
if os.getenv('LOCAL'):
    sys.stdin = open('_in.txt', 'r')
sys.setrecursionlimit(10 ** 9)
v1 = float('inf')
v2 = 10 ** 18
v3 = 10 ** 9 + 7
v4 = int(sys.stdin.buffer.readline())
v5 = list(map(int, sys.stdin.buffer.readline().split()))
v6 = list(map(int, sys.stdin.buffer.readline().split()))
v5 = np.array(v5, dtype=int)
v6 = np.array(v6, dtype=int)
v7 = v6.sum() - v5.sum()
v8 = 0
v9 = 0
for v10, v11 in zip(v5, v6):
    if v11 < v10:
        v9 += v10 - v11
    if v10 < v11:
        if (v11 - v10) % 2 == 0:
            v8 += (v11 - v10) // 2
        else:
            v8 += (v11 - v10) // 2 + 1
            v9 += 1
if v8 > v9:
    v12 = v8 - v9
    v8 += v12
    v9 += 2 * v12
v13 = v9 == v8 and v9 == v7
if v13:
    print('Yes')
else:
    print('No')
