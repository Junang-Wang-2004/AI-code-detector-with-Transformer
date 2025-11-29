import heapq

class C1:

    def minimumTime(self, a1, a2, a3):
        v1 = float('inf')
        v2 = [[] for v3 in range(a1)]
        for v4, v5, v6 in a2:
            v2[v4].append((v5, v6))
            v2[v5].append((v4, v6))
        v7 = [v1] * a1
        v7[0] = 0
        v8 = [(0, 0)]
        while v8:
            v9, v10 = heapq.heappop(v8)
            if v9 > v7[v10]:
                continue
            for v11, v12 in v2[v10]:
                v13 = v9 + v12
                if v13 < v7[v11] and v13 < a3[v11]:
                    v7[v11] = v13
                    heapq.heappush(v8, (v13, v11))
        return [-1 if d == v1 else int(d) for v14 in v7]
