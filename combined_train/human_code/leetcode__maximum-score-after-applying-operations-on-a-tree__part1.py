class C1(object):

    def maximumScoreAfterOperations(self, a1, a2):
        """
        """

        def iter_dfs():
            v1 = [0] * len(a2)
            v2 = [(1, 0, -1)]
            while v2:
                v3, v4, v5 = v2.pop()
                if v3 == 1:
                    if len(adj[v4]) == (1 if v4 else 0):
                        v1[v4] = a2[v4]
                        continue
                    v2.append((2, v4, v5))
                    for v6 in reversed(adj[v4]):
                        if v6 != v5:
                            v2.append((1, v6, v4))
                elif v3 == 2:
                    v1[v4] = min(sum((v1[v6] for v6 in adj[v4] if v6 != v5)), a2[v4])
            return v1[0]
        v1 = [[] for v2 in range(len(a2))]
        for v3, v4 in a1:
            v1[v3].append(v4)
            v1[v4].append(v3)
        return sum(a2) - iter_dfs()
