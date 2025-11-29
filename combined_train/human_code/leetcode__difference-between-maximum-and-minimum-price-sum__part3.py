class C1(object):

    def maxOutput(self, a1, a2, a3):
        """
        """

        def iter_dfs():
            v1 = [0] * a1
            v2 = [(1, 0, -1)]
            while v2:
                v3, v4, v5 = v2.pop()
                if v3 == 1:
                    v2.append((2, v4, v5))
                    for v6 in adj[v4]:
                        if v6 == v5:
                            continue
                        v2.append((1, v6, v4))
                elif v3 == 2:
                    v1[v4] = a3[v4]
                    for v6 in adj[v4]:
                        if v6 == v5:
                            continue
                        v1[v4] = max(v1[v4], v1[v6] + a3[v4])
            return v1

        def iter_dfs2():
            v1 = 0
            v2 = [(0, -1, 0)]
            while v2:
                v3, v4, v5 = v2.pop()
                v1 = max(v1, v5, dp[v3] - a3[v3])
                v6 = [[v5, v4], [0, -1]]
                for v7 in adj[v3]:
                    if v7 == v4:
                        continue
                    v5 = [dp[v7], v7]
                    for v8 in range(len(v6)):
                        if v5 > v6[v8]:
                            v6[v8], v5 = (v5, v6[v8])
                for v7 in adj[v3]:
                    if v7 == v4:
                        continue
                    v2.append((v7, v3, (v6[0][0] if v6[0][1] != v7 else v6[1][0]) + a3[v3]))
            return v1
        v1 = [[] for v2 in range(a1)]
        for v3, v4 in a2:
            v1[v3].append(v4)
            v1[v4].append(v3)
        v5 = iter_dfs()
        return iter_dfs2()
