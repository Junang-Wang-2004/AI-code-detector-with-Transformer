import heapq
v1 = int(input())
v2 = list(map(int, input().split()))
v3 = []
v4 = []
v5 = []
for v6 in range(v1):
    if not v3 or v2[v6] < -heapq.heappop(v3):
        heapq.heappush(v3, -v2[v6])
    else:
        heapq.heappush(v4, v2[v6])
    if len(v3) > len(v4) + 1:
        heapq.heappush(v4, -heapq.heappop(v3))
    elif len(v4) > len(v3):
        heapq.heappush(v3, -heapq.heappop(v4))
    if v6 >= v1 // 2:
        v5.append(-v3[0])
for v6 in range(v1 // 2):
    v5.append(v5[v6])
for v7 in v5:
    print(v7)
