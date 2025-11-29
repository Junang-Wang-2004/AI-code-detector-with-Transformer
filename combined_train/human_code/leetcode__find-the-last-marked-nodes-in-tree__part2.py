class C1(object):

    def lastMarkedNodes(self, a1):
        """
        """

        def increase(a1):
            return (a1[0] + 1, a1[1])

        def bfs():
            v1 = [[(0, u)] * 2 for v2 in range(len(adj))]
            v3 = -1
            v4 = list(map(len, adj))
            v5 = [v2 for v2 in range(len(v4)) if v4[v2] == 1]
            while v5:
                v6 = []
                for v2 in v5:
                    if v4[v2] == 0:
                        v3 = v2
                        continue
                    v4[v2] -= 1
                    for v7 in adj[v2]:
                        if v4[v7] == 0:
                            continue
                        v8 = increase(v1[v2][0])
                        for v9 in range(len(v1[v7])):
                            if v8 > v1[v7][v9]:
                                v8, v1[v7][v9] = (v1[v7][v9], v8)
                        v4[v7] -= 1
                        if v4[v7] == 1:
                            v6.append(v7)
                v5 = v6
            return (v1, v3)

        def bfs2(a1):
            v1 = [-1] * len(adj)
            v2 = [(a1, -1, (0, -1))]
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
        v5, v3 = bfs()
        return bfs2(v3)
