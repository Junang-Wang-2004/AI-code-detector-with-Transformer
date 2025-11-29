from heapq import *
v1, = map(int, input().split())
v2 = [int(input()) for v3 in range(v1)]
v4 = [0] * 7 ** 6
v5 = [[] for v3 in v4]
v6 = 0
for v7, v8 in enumerate(v2):
    v5[v8] += [v7]
for v7 in range(len(v4)):
    if v5[v7]:
        for v9 in v5[v7]:
            heappush(v4, -v9)
        v6 -= heappop(v4)
print(v6)
