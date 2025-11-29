from heapq import heappush, heappop
from collections import defaultdict as dd
v1, v2 = map(int, input().split())
v3 = dd(list)
for v4 in range(v1):
    v5, v6 = map(int, input().split())
    v3[v5].append(-v6)
v7 = []
v8 = 0
for v5 in range(1, v2 + 1):
    for v6 in v3[v5]:
        heappush(v7, v6)
    if len(v7):
        v8 -= heappop(v7)
print(v8)
