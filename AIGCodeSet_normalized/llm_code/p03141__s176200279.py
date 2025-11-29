import heapq
import sys
v1 = int(input())
v2, v3 = ([], [])
for v4 in range(v1):
    v5, v6 = map(int, input().split())
    heapq.heappush(v2, (-(v5 - v6), v5, v4))
    heapq.heappush(v3, (-(v5 - v6), v6, v4))
v7 = []
v8 = []
v9 = set([-1])
for v4 in reversed(range(v1)):
    if v4 % 2 == 1:
        v10 = 10000000000.0
        v11 = -1
        while v11 in v9 and v3:
            v12, v13, v11 = heapq.heappop(v3)
        v9.add(v11)
        v7.append(v13)
    else:
        v10 = 10000000000.0
        v11 = -1
        while v11 in v9 and v2:
            v12, v13, v11 = heapq.heappop(v2)
        v9.add(v11)
        v8.append(v13)
print(sum(v8) - sum(v7))
