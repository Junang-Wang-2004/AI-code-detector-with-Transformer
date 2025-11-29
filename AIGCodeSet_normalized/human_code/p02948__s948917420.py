import heapq
v1, v2 = map(int, input().split())
v3 = [[] for v4 in range(v2)]
for v4 in range(v1):
    v5, v6 = map(int, input().split())
    if v5 <= v2:
        v3[v5 - 1].append(-v6)
v7 = 0
v8 = []
for v9 in range(v2):
    for v10 in v3[v9]:
        heapq.heappush(v8, v10)
    if len(v8) != 0:
        v7 += heapq.heappop(v8)
print(abs(v7))
