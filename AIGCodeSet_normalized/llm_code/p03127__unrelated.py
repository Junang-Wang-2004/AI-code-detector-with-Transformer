import heapq
v1 = int(input())
v2 = list(map(int, input().split()))
heapq.heapify(v2)
while len(v2) > 1:
    v3 = heapq.heappop(v2)
    v4 = heapq.heappop(v2)
    heapq.heappush(v2, max(0, v4 - v3))
print(v2[0])
