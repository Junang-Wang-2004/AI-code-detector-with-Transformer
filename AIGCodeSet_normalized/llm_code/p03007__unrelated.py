import heapq
v1 = int(input())
v2 = list(map(int, input().split()))
heapq.heapify(v2)
v3 = 0
v4 = []
for v5 in range(v1 - 1):
    v6 = heapq.heappop(v2)
    v7 = heapq.heappop(v2)
    v3 = v6 - v7
    heapq.heappush(v2, v3)
    v4.append((v6, v7))
print(v3)
for v6, v7 in v4:
    print(v6, v7)
