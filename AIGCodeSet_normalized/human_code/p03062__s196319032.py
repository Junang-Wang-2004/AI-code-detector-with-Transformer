import heapq
import sys
input = lambda: sys.stdin.readline().rstrip()
v1 = int(input())
v2 = list(map(int, input().split()))
v3 = []
heapq.heapify(v3)
v4 = 0
v5 = False
for v6 in v2:
    if v6 == 0:
        v5 = True
    if v6 < 0:
        v4 += 1
    heapq.heappush(v3, abs(v6))
if v4 % 2 == 0 or v5:
    print(sum(v3))
else:
    v7 = heapq.heappop(v3)
    print(sum(v3) - v7)
