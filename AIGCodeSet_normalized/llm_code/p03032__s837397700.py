from copy import deepcopy
from collections import deque
from functools import partial, lru_cache
from heapq import heappush, heappop
v1 = open(0).readlines()
v2, v3 = map(int, v1[0].split())
v4 = deque(map(int, v1[1].split()))
v5 = []

def f1(a1, a2):
    v1, v2 = a1
    if v1 + v2 < a2:
        return ((v1 + 1, v2), (v1, v2 + 1))
    return tuple()

def f2(a1, a2, a3, a4, a5, a6):
    if a1 in a6:
        return max(a2, a6[a1])
    v1, v2 = a1
    v3 = deepcopy(a3)
    v4 = deepcopy(a4)
    for v5 in range(v2):
        if v4:
            heappush(v3, v4.pop())
    for v5 in range(v1):
        if v4:
            heappush(v3, v4.popleft())
    v6 = sum(v3)
    for v5 in range(min(a5 - v1 - v2, v1 + v2)):
        if v3 and v3[0] < 0:
            v6 -= heappop(v3)
    a6[a1] = v6
    return max(a2, a6[a1])

def f3(a1, a2, a3):
    v1, v2 = ([], [a1])
    v3 = 0
    while v2:
        v4 = v2.pop()
        if v4 in v1:
            continue
        v3 = a3(v4, v3)
        for v5 in a2(v4):
            if v5 not in v1:
                v2.append(v5)
    return v3
v6 = f3((0, 0), partial(f1, k=v3), partial(f2, W=v5, V=v4, k=v3, memo={}))
print(v6)
