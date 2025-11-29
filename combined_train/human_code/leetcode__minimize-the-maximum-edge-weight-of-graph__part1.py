import collections
import heapq

class C1(object):

    def minMaxWeight(self, a1, a2, a3):
        """
        """

        def dijkstra():
            v1 = [float('inf')] * len(adj)
            v1[0] = 0
            v2 = [(v1[0], 0)]
            while v2:
                v3, v4 = heapq.heappop(v2)
                if v3 != v1[v4]:
                    continue
                for v5, v6 in adj[v4].items():
                    if not max(v3, v6) < v1[v5]:
                        continue
                    v1[v5] = max(v3, v6)
                    heapq.heappush(v2, (v1[v5], v5))
            v7 = max(v1)
            return v7 if v7 != float('inf') else -1
        v1 = [collections.defaultdict(lambda: float('inf')) for v2 in range(a1)]
        for v3, v4, v5 in a2:
            v1[v4][v3] = min(v1[v4][v3], v5)
        return dijkstra()
