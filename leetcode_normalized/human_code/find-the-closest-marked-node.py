import heapq

class C1(object):

    def minimumDistance(self, a1, a2, a3, a4):
        """
        """

        def dijkstra(a1):
            v1 = [float('inf')] * len(adj)
            v1[a1] = 0
            v2 = [(0, a1)]
            while v2:
                v3, v4 = heapq.heappop(v2)
                if v3 > v1[v4]:
                    continue
                if v4 in target:
                    return v3
                for v5, v6 in adj[v4]:
                    if v3 + v6 >= v1[v5]:
                        continue
                    v1[v5] = v3 + v6
                    heapq.heappush(v2, (v1[v5], v5))
            return -1
        v1 = set(a4)
        v2 = [[] for v3 in range(a1)]
        for v4, v5, v6 in a2:
            v2[v4].append((v5, v6))
        return dijkstra(a3)
