import heapq
v1, v2 = map(int, input().split())
v3 = []
for v4 in range(v1):
    v5, v6, v7 = map(int, input().split())
    v3.append((v5, v6, v7))
v3.sort()
v8 = []
v9 = 0
for v5, v6, v7 in v3:
    while v8 and v8[0][0] <= v5 - 0.5:
        heapq.heappop(v8)
    if len(v8) < v2:
        v9 += 1
        heapq.heappush(v8, (v6, v7))
    else:
        for v4 in range(len(v8)):
            if v8[v4][1] == v7:
                heapq.heapreplace(v8, (v6, v7))
                break
        else:
            v9 += 1
            heapq.heappush(v8, (v6, v7))
print(v9)
