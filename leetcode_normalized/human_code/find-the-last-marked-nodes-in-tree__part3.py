class C1(object):

    def lastMarkedNodes(self, a1):
        """
        """

        def increase(a1):
            return (a1[0] + 1, a1[1])

        def topological_traversal():
            v1 = [-2] * len(adj)
            v1[0] = -1
            v2 = [0]
            for v3 in v2:
                for v4 in reversed(adj[v3]):
                    if v1[v4] != -2:
                        continue
                    v1[v4] = v3
                    v2.append(v4)
            v5 = [[(0, v3)] * 2 for v3 in range(len(adj))]
            for v3 in reversed(v2):
                for v4 in adj[v3]:
                    if v4 == v1[v3]:
                        continue
                    v6 = increase(v5[v4][0])
                    for v7 in range(len(v5[v3])):
                        if v6 > v5[v3][v7]:
                            v6, v5[v3][v7] = (v5[v3][v7], v6)
            return v5

        def bfs():
            v1 = [-1] * len(adj)
            v2 = [(0, -1, (0, -1))]
            while v2:
                v3 = []
                for v4, v5, v6 in v2:
                    v1[v4] = max(dp[v4][0], v6)[1]
                    for v7 in adj[v4]:
                        if v7 == v5:
                            continue
                        v3.append((v7, v4, increase(max(dp[v4][dp[v4][0][1] == dp[v7][0][1]], v6))))
                v2 = v3
            return v1
        v1 = [[] for v2 in range(len(a1) + 1)]
        for v3, v4 in a1:
            v1[v3].append(v4)
            v1[v4].append(v3)
        v5 = topological_traversal()
        return bfs()
