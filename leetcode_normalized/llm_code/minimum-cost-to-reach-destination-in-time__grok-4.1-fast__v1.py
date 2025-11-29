import heapq

class C1(object):

    def minCost(self, a1, a2, a3):
        v1 = len(a3)
        v2 = [[] for v3 in range(v1)]
        for v4, v5, v6 in a2:
            v2[v4].append((v5, v6))
            v2[v5].append((v4, v6))
        v7 = [float('inf')] * v1
        v7[0] = 0
        v8 = []
        heapq.heappush(v8, (a3[0], 0, 0))
        while v8:
            v9, v10, v11 = heapq.heappop(v8)
            if v11 > a1:
                continue
            if v10 == v1 - 1:
                return v9
            for v12, v13 in v2[v10]:
                v14 = v11 + v13
                if v14 < v7[v12]:
                    v7[v12] = v14
                    heapq.heappush(v8, (v9 + a3[v12], v12, v14))
        return -1
