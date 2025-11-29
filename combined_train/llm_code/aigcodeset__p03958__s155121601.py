import heapq
if __name__ == '__main__':
    v1, v2 = map(int, input().split())
    v3 = list(map(int, input().split()))
    v4 = []
    for v5, v6 in enumerate(v3):
        v4.append([v6, v5])
    heapq._heapify_max(v4)
    while len(v4) > 1:
        v7 = heapq._heappop_max(v4)
        v8 = heapq._heappop_max(v4)
        v7[0] -= 1
        v8[0] -= 1
        if v7[0] > 0:
            heapq.heappush(v4, v7)
        if v8[0] > 0:
            heapq.heappush(v4, v8)
    v9 = 0
    if len(v4) > 0:
        v9 = v4[0][0]
    print(max(0, v9 - 1))
