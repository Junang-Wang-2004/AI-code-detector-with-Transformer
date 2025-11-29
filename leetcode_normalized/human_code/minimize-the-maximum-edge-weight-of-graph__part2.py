import collections
import heapq

class C1(object):

    def minMaxWeight(self, a1, a2, a3):
        """
        """

        def prim():
            v1 = [float('inf')] * len(adj)
            v2 = [(0, 0)]
            while v2:
                v3, v4 = heapq.heappop(v2)
                if v1[v4] != float('inf'):
                    continue
                v1[v4] = v3
                for v5, v6 in adj[v4].items():
                    if v1[v5] != float('inf'):
                        continue
                    heapq.heappush(v2, (v6, v5))
            v7 = max(v1)
            return v7 if v7 != float('inf') else -1
        v1 = [collections.defaultdict(lambda: float('inf')) for v2 in range(a1)]
        for v3, v4, v5 in a2:
            v1[v4][v3] = min(v1[v4][v3], v5)
        return prim()
