import heapq

class C1(object):

    def __init__(self, a1, a2):
        """
        """
        self.__adj = [[] for v1 in range(a1)]
        for v2 in a2:
            self.addEdge(v2)

    def addEdge(self, a1):
        """
        """
        v1, v2, v3 = a1
        self.__adj[v1].append((v2, v3))

    def shortestPath(self, a1, a2):
        """
        """

        def dijkstra(a1, a2, a3):
            v1 = [float('inf')] * len(a1)
            v1[a2] = 0
            v2 = [(v1[a2], a2)]
            while v2:
                v3, v4 = heapq.heappop(v2)
                if v3 > v1[v4]:
                    continue
                for v5, v6 in a1[v4]:
                    if not v3 + v6 < v1[v5]:
                        continue
                    v1[v5] = v3 + v6
                    heapq.heappush(v2, (v1[v5], v5))
            return v1[a3] if v1[a3] != float('inf') else -1
        return dijkstra(self.__adj, a1, a2)
