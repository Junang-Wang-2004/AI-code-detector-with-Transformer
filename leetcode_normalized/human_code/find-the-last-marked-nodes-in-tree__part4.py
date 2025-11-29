class C1(object):

    def lastMarkedNodes(self, a1):
        """
        """

        def increase(a1):
            return (a1[0] + 1, a1[1])

        def iter_dfs1():
            v1 = [[(0, u)] * 2 for v2 in range(len(adj))]
            v3 = [(1, (0, -1))]
            while v3:
                v4, v5 = v3.pop()
                if v4 == 1:
                    v2, v6 = v5
                    v3.append((2, (v2, v6, 0)))
                elif v4 == 2:
                    v2, v6, v7 = v5
                    if v7 == len(adj[v2]):
                        continue
                    v3.append((2, (v2, v6, v7 + 1)))
                    v8 = adj[v2][v7]
                    if v8 == v6:
                        continue
                    v3.append((3, (v8, v2)))
                    v3.append((1, (v8, v2)))
                elif v4 == 3:
                    v8, v2 = v5
                    v9 = increase(v1[v8][0])
                    for v7 in range(len(v1[v2])):
                        if v9 > v1[v2][v7]:
                            v9, v1[v2][v7] = (v1[v2][v7], v9)
            return v1

        def iter_dfs2():
            v1 = [-1] * len(adj)
            v2 = [(0, -1, (0, -1))]
            while v2:
                v3, v4, v5 = v2.pop()
                v1[v3] = max(dp[v3][0], v5)[1]
                for v6 in reversed(adj[v3]):
                    if v6 == v4:
                        continue
                    v2.append((v6, v3, increase(max(dp[v3][dp[v3][0][1] == dp[v6][0][1]], v5))))
            return v1
        v1 = [[] for v2 in range(len(a1) + 1)]
        for v3, v4 in a1:
            v1[v3].append(v4)
            v1[v4].append(v3)
        v5 = iter_dfs1()
        return iter_dfs2()
