class C1(object):

    def treeDiameter(self, a1):
        """
        """

        def iter_dfs():
            v1 = 0
            v2 = [(1, (0, -1, [0]))]
            while v2:
                v3, v4 = v2.pop()
                if v3 == 1:
                    v5, v6, v7 = v4
                    for v8 in reversed(adj[v5]):
                        if v8 == v6:
                            continue
                        v9 = [0]
                        v2.append((2, (v9, v7)))
                        v2.append((1, (v8, v5, v9)))
                elif v3 == 2:
                    v9, v7 = v4
                    v1 = max(v1, v7[0] + (v9[0] + 1))
                    v7[0] = max(v7[0], v9[0] + 1)
            return v1
        v1 = [[] for v2 in range(len(a1) + 1)]
        for v3, v4 in a1:
            v1[v3].append(v4)
            v1[v4].append(v3)
        return iter_dfs()
