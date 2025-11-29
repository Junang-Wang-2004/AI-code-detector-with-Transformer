import heapq

class C1(object):

    def shortestDistanceAfterQueries(self, a1, a2):
        """
        """

        def dijkstra(a1, a2):
            adj[a1].append((a2, 1))
            v1 = [(dist[a1], a1)]
            while v1:
                v2, a1 = heapq.heappop(v1)
                if v2 > dist[a1]:
                    continue
                for a2, v5 in adj[a1]:
                    if v2 + v5 >= dist[a2]:
                        continue
                    dist[a2] = v2 + v5
                    heapq.heappush(v1, (dist[a2], a2))
            return dist[-1]
        v1 = [[] for v2 in range(a1)]
        for v3 in range(a1 - 1):
            v1[v3].append((v3 + 1, 1))
        v4 = list(range(a1))
        return [dijkstra(v3, v) for v3, v5 in a2]
