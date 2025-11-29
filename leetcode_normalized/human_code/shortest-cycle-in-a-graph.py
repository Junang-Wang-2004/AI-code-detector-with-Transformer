class C1(object):

    def findShortestCycle(self, a1, a2):
        """
        """
        v1 = float('inf')

        def bfs(a1):
            v1 = v1
            v2 = [float('inf')] * len(adj)
            v2[a1] = 0
            v3 = [a1]
            while v3:
                v4 = []
                for a1 in v3:
                    for v6 in adj[a1]:
                        if v2[v6] != v1:
                            assert abs(v2[v6] - v2[a1]) <= 1
                            if v2[v6] != v2[a1] - 1:
                                v1 = min(v1, 1 + v2[a1] + v2[v6])
                            continue
                        v2[v6] = v2[a1] + 1
                        v4.append(v6)
                if v1 != v1:
                    break
                v3 = v4
            return v1
        v2 = [[] for v3 in range(a1)]
        for v4, v5 in a2:
            v2[v4].append(v5)
            v2[v5].append(v4)
        v6 = min((bfs(v4) for v4 in range(a1)))
        return v6 if v6 != v1 else -1
