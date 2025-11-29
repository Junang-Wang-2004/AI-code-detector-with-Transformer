import heapq
v1, v2 = map(int, input().split())
v3 = [0] * v1
v4 = [0] * v1
v5 = [[] for v6 in range(v2 + 1)]
v7 = 0
for v8 in range(v1):
    if v8 <= v2:
        heapq.heapify(v5[v8])
    v3[v8], v4[v8] = map(int, input().split())
    if v3[v8] <= v2:
        v5[v3[v8]].append(-v4[v8])
for v9 in range(1, v2 + 1):
    for v8 in range(len(v5[v9])):
        heapq.heappush(v5[0], v5[v9][v8])
    if v5[0]:
        v7 += heapq.heappop(v5[0])
print(-v7)
