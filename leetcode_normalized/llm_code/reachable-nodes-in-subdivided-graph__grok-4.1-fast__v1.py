import heapq

class C1(object):

    def reachableNodes(self, a1, a2, a3):
        v1 = [[] for v2 in range(a3)]
        for v3, v4, v5 in a1:
            v1[v3].append((v4, v5))
            v1[v4].append((v3, v5))
        v6 = [float('inf')] * a3
        v6[0] = 0
        v7 = []
        heapq.heappush(v7, (0, 0))
        while v7:
            v8, v9 = heapq.heappop(v7)
            if v8 > v6[v9]:
                continue
            for v10, v11 in v1[v9]:
                v12 = v8 + v11 + 1
                if v12 <= a2 and v12 < v6[v10]:
                    v6[v10] = v12
                    heapq.heappush(v7, (v12, v10))
        v13 = sum((1 for v14 in v6 if v14 <= a2))
        for v3, v4, v5 in a1:
            v15 = max(0, a2 - v6[v3]) if v6[v3] <= a2 else 0
            v16 = max(0, a2 - v6[v4]) if v6[v4] <= a2 else 0
            v13 += min(v5, v15 + v16)
        return v13
