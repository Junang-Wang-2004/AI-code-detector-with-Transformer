import heapq
v1, v2 = map(int, input().split())
v3 = []
for v4 in range(v1):
    v5, v6 = map(int, input().split())
    heapq.heappush(v3, (v5, v6))
v7 = 0
while v3:
    v8, v9 = heapq.heappop(v3)
    if v7 + v9 < v2:
        v7 += v9
    else:
        print(v8)
        break
