class C1(object):

    def timeTaken(self, a1):
        """
        """

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
            for v3 in reversed(v2):
                for v4 in adj[v3]:
                    if v4 == v1[v3]:
                        continue
                    v5 = [1 + int(v4 % 2 == 0) + dp[v4][0][0], v4]
                    for v6 in range(len(dp[v3])):
                        if v5 > dp[v3][v6]:
                            v5, dp[v3][v6] = (dp[v3][v6], v5)

        def bfs():
            v1 = [(0, -1, 0)]
            while v1:
                v2 = []
                for v3, v4, v5 in v1:
                    result[v3] = max(dp[v3][0][0], v5)
                    for v6 in adj[v3]:
                        if v6 == v4:
                            continue
                        v2.append((v6, v3, 1 + int(v3 % 2 == 0) + max(dp[v3][0][0] if dp[v3][0][1] != v6 else dp[v3][1][0], v5)))
                v1 = v2
        v1 = [[] for v2 in range(len(a1) + 1)]
        for v3, v4 in a1:
            v1[v3].append(v4)
            v1[v4].append(v3)
        v5 = [[[0, -1] for v2 in range(2)] for v2 in range(len(a1) + 1)]
        topological_traversal()
        v6 = [0] * (len(a1) + 1)
        bfs()
        return v6
