class C1(object):

    def maxScore(self, a1):
        """
        """

        def iter_dfs():
            v1 = [(0, 0) for v2 in range(len(adj))]
            v3 = [(1, 0)]
            while v3:
                v4, v5 = v3.pop()
                if v4 == 1:
                    if not adj[v5]:
                        continue
                    v3.append((2, v5))
                    for v6, v2 in adj[v5]:
                        v3.append((1, v6))
                elif v4 == 2:
                    v7 = sum((max(v1[v6]) for v6, v8 in adj[v5]))
                    v9 = max((v7 - max(v1[v6]) + (v1[v6][1] + v8) for v6, v8 in adj[v5]))
                    v1[v5] = (v9, v7)
            return max(v1[0])
        v1 = [[] for v2 in range(len(a1))]
        for v3, (v4, v5) in enumerate(a1):
            if v3 == 0:
                continue
            v1[v4].append((v3, v5))
        return iter_dfs()
