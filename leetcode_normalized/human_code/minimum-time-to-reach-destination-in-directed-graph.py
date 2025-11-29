import heapq

class C1(object):

    def minTime(self, a1, a2):
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
                for v5, v6, v7 in adj[v4]:
                    if v3 > v7:
                        continue
                    if not v1[v5] > max(v3, v6) + 1:
                        continue
                    v1[v5] = max(v3, v6) + 1
                    heapq.heappush(v2, (v1[v5], v5))
            return -1
        v1 = [[] for v2 in range(a1)]
        for v3, v4, v5, v6 in a2:
            v1[v3].append((v4, v5, v6))
        return dijkstra()
