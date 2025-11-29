from itertools import accumulate
import heapq as hq
v1, v2 = map(int, input().split())
v3 = [list(map(int, input().split())) for v4 in range(v1)]
v3.sort()
v5 = []
hq.heapify(v5)
v6 = max([a[0] for v7 in v3])
v8 = [0] * (v6 + 1)
for v4 in range(v1):
    v8[v3[v4][0]] += 1
v9 = list(accumulate(v8))
v10 = 0
for v4 in range(1, v2 + 1):
    for v11 in range(v9[v4 - 1], v9[v4]):
        hq.heappush(v5, -v3[v11][1])
    if v5:
        v10 -= hq.heappop(v5)
print(v10)
