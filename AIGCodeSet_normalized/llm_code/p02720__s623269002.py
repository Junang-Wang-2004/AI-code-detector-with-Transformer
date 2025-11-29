v1 = int(input())
import heapq
v2 = []
for v3 in range(1, 10):
    heapq.heappush(v2, v3)
v4 = 0
while True:
    v4 += 1
    v5 = heapq.heappop(v2)
    v6 = v5 % 10
    if v6 > 0:
        heapq.heappush(v2, v5 * 10 + v6 - 1)
    if v6 < 9:
        heapq.heappush(v2, v5 * 10 + v6 + 1)
    heapq.heappush(v2, v5 * 10 + v6)
    if v4 == v1:
        print(v5)
        exit()
