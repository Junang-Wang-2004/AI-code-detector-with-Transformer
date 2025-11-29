import heapq

class C1(object):

    def minCost(self, a1, a2):
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
                if v4 == len(adj) - 1:
                    return v3
                for v5, v6 in adj[v4]:
                    if not v1[v5] > v3 + v6:
                        continue
                    v1[v5] = v3 + v6
                    heapq.heappush(v2, (v1[v5], v5))
            return -1
        v1 = [[] for v2 in range(a1)]
        for v3, v4, v5 in a2:
            v1[v3].append((v4, v5))
            v1[v4].append((v3, 2 * v5))
        return dijkstra()
