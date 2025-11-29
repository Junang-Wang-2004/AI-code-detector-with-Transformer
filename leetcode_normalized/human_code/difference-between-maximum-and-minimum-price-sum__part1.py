class C1(object):

    def maxOutput(self, a1, a2, a3):
        """
        """

        def iter_dfs():
            v1 = 0
            v2 = [(1, (0, -1, [a3[0], 0]))]
            while v2:
                v3, v4 = v2.pop()
                if v3 == 1:
                    v5, v6, v7 = v4
                    v2.append((2, (v5, v6, v7, 0)))
                elif v3 == 2:
                    v5, v6, v7, v8 = v4
                    if v8 == len(adj[v5]):
                        continue
                    v2.append((2, (v5, v6, v7, v8 + 1)))
                    v9 = adj[v5][v8]
                    if v9 == v6:
                        continue
                    v10 = [a3[v9], 0]
                    v2.append((3, (v5, v10, v7)))
                    v2.append((1, (v9, v5, v10)))
                elif v3 == 3:
                    v5, v10, v7 = v4
                    v1 = max(v1, v7[0] + v10[1], v7[1] + v10[0])
                    v7[0] = max(v7[0], v10[0] + a3[v5])
                    v7[1] = max(v7[1], v10[1] + a3[v5])
            return v1
        v1 = [[] for v2 in range(a1)]
        for v3, v4 in a2:
            v1[v3].append(v4)
            v1[v4].append(v3)
        return iter_dfs()
