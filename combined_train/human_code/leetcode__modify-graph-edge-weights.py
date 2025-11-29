import heapq

class C1(object):

    def modifiedGraphEdges(self, a1, a2, a3, a4, a5):
        """
        """

        def dijkstra(a1, a2):
            v1 = [a5 + 1] * len(adj)
            v1[a1] = 0
            v2 = [(0, a1)]
            while v2:
                v3, v4 = heapq.heappop(v2)
                if v3 > v1[v4]:
                    continue
                for v5, v6 in adj[v4]:
                    if v6 == -1:
                        v6 = a2
                    if v3 + v6 >= v1[v5]:
                        continue
                    v1[v5] = v3 + v6
                    heapq.heappush(v2, (v1[v5], v5))
            return v1
        v1 = [[] for v2 in range(a1)]
        for v3, v4, v5 in a2:
            v1[v3].append((v4, v5))
            v1[v4].append((v3, v5))
        v6 = dijkstra(a3, 1)
        if not v6[a4] <= a5:
            return []
        v7 = dijkstra(a4, a5 + 1)
        if not v7[a3] >= a5:
            return []
        for v8 in a2:
            if v8[2] == -1:
                v8[2] = max(a5 - v6[v8[0]] - v7[v8[1]], a5 - v6[v8[1]] - v7[v8[0]], 1)
        return a2
