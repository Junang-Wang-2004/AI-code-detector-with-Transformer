def f1(a1, a2):
    v1 = [(0, a1)]
    v2 = set([a1])
    v3 = 0
    while v1:
        v3, v4 = heapq.heappop(v1)
        v5 = [(L, v4)]
        v6 = set([v4])
        while v5:
            v7, v8 = heapq.heappop(v5)
            for v9 in g[v8]:
                if g[v8][v9] > v7:
                    continue
                if v9 in v6 or v9 in v2:
                    continue
                v5.append((v7 - g[v8][v9], v9))
                v6.add(v9)
        if a2 in v6:
            return v3
        v2 |= v6
        for v10 in v6:
            heapq.heappush(v1, (v3 + 1, v10))
    return -1
