import heapq

class C1(object):

    def networkDelayTime(self, a1, a2, a3):
        v1 = [[] for v2 in range(a2)]
        for v3, v4, v5 in a1:
            v1[v3 - 1].append((v4 - 1, v5))
        v6 = [float('inf')] * a2
        v6[a3 - 1] = 0
        v7 = [(0, a3 - 1)]
        while v7:
            v8, v3 = heapq.heappop(v7)
            if v8 > v6[v3]:
                continue
            for v4, v9 in v1[v3]:
                v10 = v8 + v9
                if v10 < v6[v4]:
                    v6[v4] = v10
                    heapq.heappush(v7, (v10, v4))
        v11 = max(v6)
        return v11 if v11 < float('inf') else -1
