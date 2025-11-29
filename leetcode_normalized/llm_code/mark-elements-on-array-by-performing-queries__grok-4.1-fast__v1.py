class C1:

    def unmarkedSumArray(self, a1, a2):
        v1 = len(a1)
        v2 = 0
        for v3 in a1:
            v2 += v3
        v4 = [False] * v1
        v5 = []
        for v6 in range(v1):
            heapq.heappush(v5, (a1[v6], v6))
        v7 = []
        for v8, v9 in a2:
            if not v4[v8]:
                v4[v8] = True
                v2 -= a1[v8]
            v10 = 0
            while v10 < v9 and v5:
                v11, v12 = heapq.heappop(v5)
                if v4[v12]:
                    continue
                v4[v12] = True
                v2 -= v11
                v10 += 1
            v7.append(v2)
        return v7
