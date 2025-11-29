import heapq
v1, v2 = (int(x) for v3 in input().split())
v4 = list((-1 * int(v3) for v3 in input().split()))
heapq.heapify(v4)
for v5 in range(v2):
    if len(v4) == 1:
        print(0)
        break
    heapq.heappop(v4)
if len(v4) != 1:
    sum = 0
    while len(v4) > 0:
        sum -= heapq.heappop(v4)
    print(sum)
