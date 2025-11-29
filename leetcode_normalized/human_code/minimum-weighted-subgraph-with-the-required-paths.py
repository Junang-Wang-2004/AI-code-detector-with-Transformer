import heapq

class C1(object):

    def minimumWeight(self, a1, a2, a3, a4, a5):
        """
        """

        def dijkstra(a1, a2):
            v1 = [float('inf')] * len(a1)
            v1[a2] = 0
            v2 = [(0, a2)]
            while v2:
                v3, v4 = heapq.heappop(v2)
                if v1[v4] < v3:
                    continue
                for v5, v6 in a1[v4]:
                    if v1[v5] <= v3 + v6:
                        continue
                    v1[v5] = v3 + v6
                    heapq.heappush(v2, (v3 + v6, v5))
            return v1
        v1, v2 = [[[] for v3 in range(a1)] for v3 in range(2)]
        for v4, v5, v6 in a2:
            v1[v4].append((v5, v6))
            v2[v5].append((v4, v6))
        v7 = dijkstra(v1, a3)
        v8 = dijkstra(v1, a4)
        v9 = dijkstra(v2, a5)
        v10 = min((v7[i] + v8[i] + v9[i] for v11 in range(a1)))
        return v10 if v10 != float('inf') else -1
