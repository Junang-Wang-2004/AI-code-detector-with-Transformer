class C1(object):

    def shortestDistanceAfterQueries(self, a1, a2):
        """
        """

        def bfs(a1, a2):
            adj[a1].append(a2)
            v1 = [a1]
            while v1:
                v2 = []
                for a1 in v1:
                    for a2 in adj[a1]:
                        if dist[a1] + 1 >= dist[a2]:
                            continue
                        dist[a2] = dist[a1] + 1
                        v2.append(a2)
                v1 = v2
            return dist[-1]
        v1 = [[] for v2 in range(a1)]
        for v3 in range(a1 - 1):
            v1[v3].append(v3 + 1)
        v4 = list(range(a1))
        return [bfs(v3, v) for v3, v5 in a2]
