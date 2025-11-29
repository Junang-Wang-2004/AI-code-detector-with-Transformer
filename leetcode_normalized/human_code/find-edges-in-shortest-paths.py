import heapq

class C1(object):

    def findAnswer(self, a1, a2):
        """
        """
        v1 = float('inf')

        def dijkstra(a1):
            v1 = [v1] * len(adj)
            v1[a1] = 0
            v2 = [(0, a1)]
            while v2:
                v3, v4 = heapq.heappop(v2)
                if v3 > v1[v4]:
                    continue
                for v5, v6 in adj[v4]:
                    if v1[v5] <= v3 + v6:
                        continue
                    v1[v5] = v3 + v6
                    heapq.heappush(v2, (v1[v5], v5))
            return v1
        v2 = [[] for v3 in range(a1)]
        for v4, v5, v6 in a2:
            v2[v4].append((v5, v6))
            v2[v5].append((v4, v6))
        v7 = dijkstra(0)
        v8 = dijkstra(a1 - 1)
        return [v7[v4] != v1 != v8[v5] and v7[v4] + v6 + v8[v5] == v7[a1 - 1] or (v8[v4] != v1 != v7[v5] and v8[v4] + v6 + v7[v5] == v8[0]) for v9, (v4, v5, v6) in enumerate(a2)]
