v1 = lambda: map(int, input().split())
v2 = lambda: list(map(int, input().split()))
v3 = lambda: tuple(map(int, input().split()))
v4 = lambda: int(input())
v5 = lambda fl: print('Yes') if fl else print('No')
import collections
import math
import itertools
import heapq as hq
v6 = v4()
if v6 == 1:
    print(1)
    exit()
v7 = []
for v8 in range(v6):
    v7.append(v3())
v9 = collections.Counter()
for v8 in range(v6):
    for v10 in range(v6):
        if v8 == v10:
            continue
        v11, v12 = v7[v8]
        v13, v14 = v7[v10]
        v9[v13 - v11, v14 - v12] += 1
v15 = 10 ** 9
for v16 in v9.values():
    v15 = min(v15, v6 - v16)
print(v15)
