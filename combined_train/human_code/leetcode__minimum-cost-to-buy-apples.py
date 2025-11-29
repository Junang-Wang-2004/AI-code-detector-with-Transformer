import itertools
import heapq

class C1(object):

    def minCost(self, a1, a2, a3, a4):
        """
        """

        def dijkstra(a1):
            v1 = [float('inf')] * len(adj)
            v1[a1] = 0
            v2 = [(0, a1)]
            while v2:
                v3, v4 = heapq.heappop(v2)
                if v1[v4] < v3:
                    continue
                for v5, v6 in adj[v4]:
                    if v1[v5] <= v3 + v6:
                        continue
                    v1[v5] = v3 + v6
                    heapq.heappush(v2, (v3 + v6, v5))
            return v1
        v1 = [[] for v2 in range(a1)]
        for v3, v4, v5 in a2:
            v1[v3 - 1].append((v4 - 1, v5))
            v1[v4 - 1].append((v3 - 1, v5))
        return [min((v3 + d * (a4 + 1) for v3, v6 in zip(a3, dijkstra(u)))) for v7 in range(a1)]
