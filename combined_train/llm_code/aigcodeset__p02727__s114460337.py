import heapq
v1, v2, v3, v4, v5 = map(int, input().split())
v6 = list(map(int, input().split()))
v7 = list(map(int, input().split()))
v8 = list(map(int, input().split()))
v6.sort(reverse=True)
v7.sort(reverse=True)
v8.sort(reverse=True)
v6 = v6[:v1]
v7 = v7[:v2]
heapq.heapify(v6)
heapq.heapify(v7)
for v9 in v8:
    if len(v6) < v1 and v9 > v6[0]:
        heapq.heappush(v6, v9)
        heapq.heappop(v6)
    elif len(v7) < v2 and v9 > v7[0]:
        heapq.heappush(v7, v9)
        heapq.heappop(v7)
print(sum(v6) + sum(v7))
