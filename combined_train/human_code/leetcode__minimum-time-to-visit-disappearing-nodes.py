import heapq

class C1(object):

    def minimumTime(self, a1, a2, a3):
        """
        """
        v1 = float('inf')

        def modified_dijkstra(a1):
            v1 = [-1] * a1
            v1[a1] = 0
            v2 = [(v1[a1], a1)]
            while v2:
                v3, v4 = heapq.heappop(v2)
                if v3 != v1[v4]:
                    continue
                for v5, v6 in adj[v4]:
                    if not v3 + v6 < min(v1[v5] if v1[v5] != -1 else v1, a3[v5]):
                        continue
                    v1[v5] = v3 + v6
                    heapq.heappush(v2, (v1[v5], v5))
            return v1
        v2 = [[] for v3 in range(a1)]
        for v4, v5, v6 in a2:
            v2[v4].append((v5, v6))
            v2[v5].append((v4, v6))
        return modified_dijkstra(0)
