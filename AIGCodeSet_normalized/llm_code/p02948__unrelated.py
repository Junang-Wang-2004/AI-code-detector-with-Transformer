import heapq
v1, v2 = map(int, input().split())
v3 = [list(map(int, input().split())) for v4 in range(v1)]
v3.sort(key=lambda x: x[0])
v5 = 0
v6 = 0
v7 = []
for v8 in range(1, v2 + 1):
    while v3 and v3[0][0] == v8:
        heapq.heappush(v7, -v3[0][1])
        v3.pop(0)
    if v7:
        v6 += -heapq.heappop(v7)
    v5 = max(v5, v6)
print(v5)
