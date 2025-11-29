import heapq

class C1(object):

    def minCost(self, a1, a2, a3, a4):
        v1 = a4 + 1
        v2 = 10 ** 20
        v3 = [[] for v4 in range(a1 + 1)]
        for v5, v6, v7 in a2:
            v8 = v5 - 1
            v9 = v6 - 1
            v10 = v7 * v1
            v3[v8].append((v9, v10))
            v3[v9].append((v8, v10))
        v11 = a1
        for v12 in range(a1):
            v3[v11].append((v12, a3[v12]))
        v13 = [v2] * (a1 + 1)
        v13[v11] = 0
        v14 = [(0, v11)]
        while v14:
            v15, v16 = heapq.heappop(v14)
            if v15 > v13[v16]:
                continue
            for v17, v18 in v3[v16]:
                v19 = v15 + v18
                if v19 < v13[v17]:
                    v13[v17] = v19
                    heapq.heappush(v14, (v19, v17))
        return v13[:a1]
