import heapq

class C1(object):

    def shortestPathWithHops(self, a1, a2, a3, a4, a5):
        """
        """

        def modified_dijkstra():
            v1 = [[float('inf')] * (a5 + 1) for v2 in range(len(adj))]
            v1[a3][0] = 0
            v3 = [(v1[a3][0], a3, 0)]
            while v3:
                v4, v5, v6 = heapq.heappop(v3)
                if v4 > v1[v5][v6]:
                    continue
                if v5 == a4:
                    return v4
                for v7, v8 in adj[v5]:
                    if v4 + v8 < v1[v7][v6]:
                        v1[v7][v6] = v4 + v8
                        heapq.heappush(v3, (v1[v7][v6], v7, v6))
                    if v6 + 1 <= a5 and v4 < v1[v7][v6 + 1]:
                        v1[v7][v6 + 1] = v4
                        heapq.heappush(v3, (v1[v7][v6 + 1], v7, v6 + 1))
            return -1
        v1 = [[] for v2 in range(a1)]
        for v3, v4, v5 in a2:
            v1[v3].append((v4, v5))
            v1[v4].append((v3, v5))
        return modified_dijkstra()
