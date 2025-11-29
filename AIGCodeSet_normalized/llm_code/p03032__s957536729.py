import heapq, copy
v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = -10 ** 10
for v5 in range(min(v1, v2)):
    for v6 in range(min(v1, v2) - v5):
        v7 = []
        for v8 in range(v5):
            v7.append(v3[v8])
        for v8 in range(v6):
            v7.append(v3[-v8 - 1])
        v9 = sum(v7)
        heapq.heapify(v7)
        v4 = max(v4, v9)
        for v10 in range(min(v1, v2) - v5 - v6):
            if len(v7) <= 0:
                break
            v11 = heapq.heappop(v7)
            if v11 >= 0:
                break
            v9 -= v11
            v4 = max(v4, v9)
print(v4)
