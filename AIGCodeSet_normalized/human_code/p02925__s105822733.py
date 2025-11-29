from heapq import heappush, heappop
from collections import deque, defaultdict, Counter
import itertools
from itertools import permutations
import sys
import bisect
import string
import math
import time
v1 = time.time()
sys.setrecursionlimit(10 ** 6)

def f1():
    return input().split()

def f2():
    return map(int, input().split())

def f3():
    return int(input())

def f4():
    return [int(i) for v1 in input().split()]
v2 = ['Yes', 'No']
v3 = 10 ** 9 + 7
v4 = f3()
v5 = []
v6 = []
v7 = [0] * v4
for v8 in range(v4):
    v9 = [v8 - 1 for v8 in f4()[::-1]]
    v7[v8] = v9.pop()
    v5.append(v9)
    v6.append([-1] * v4)
v10 = True
v11 = 0
v12 = 0
v13 = set(range(v4))
v14 = set(range(v4))
while v10 and v12 < v4 * (v4 - 1) // 2:
    v15 = time.time() - v1
    if v15 > 1.8:
        v11 = v4 * (v4 - 1) // 2
        break
    v11 += 1
    v16 = False
    v17 = set()
    for v8 in v13:
        if v8 in v17 or v7[v8] in v17 or v7[v8] == v4:
            continue
        v18 = v8
        v19 = v7[v8]
        if v18 == v7[v19]:
            v16 = True
            v12 += 1
            if v5[v18]:
                v20 = v5[v18].pop()
            else:
                v20 = v4
                v14.remove(v18)
            if v5[v19]:
                v21 = v5[v19].pop()
            else:
                v21 = v4
                v14.remove(v19)
            v7[v7[v8]], v7[v8] = (v21, v20)
            v17.add(v18)
            v17.add(v19)
    v13 = [v8 for v8 in v14]
    v11 = v11 if v16 else -1
    v10 = True if v16 else False
print(v11)
