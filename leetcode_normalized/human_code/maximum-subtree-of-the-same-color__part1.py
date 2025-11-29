class C1(object):

    def maximumSubtreeSize(self, a1, a2):
        """
        """

        def iter_dfs():
            v1 = 0
            v2 = [(1, (0, -1, [1]))]
            while v2:
                v3, v4 = v2.pop()
                if v3 == 1:
                    v5, v6, v7 = v4
                    v2.append((4, (v7,)))
                    v2.append((2, (v5, v6, v7, 0)))
                elif v3 == 2:
                    v5, v6, v7, v8 = v4
                    if v8 == len(adj[v5]):
                        continue
                    v9 = adj[v5][v8]
                    v2.append((2, (v5, v6, v7, v8 + 1)))
                    if v9 == v6:
                        continue
                    v10 = [1]
                    v2.append((3, (v9, v5, v10, v7)))
                    v2.append((1, (v9, v5, v10)))
                elif v3 == 3:
                    v9, v5, v10, v7 = v4
                    if v7[0] == -1:
                        continue
                    if v10[0] == 0 or a2[v9] != a2[v5]:
                        v7[0] = -1
                        continue
                    v7[0] += v10[0]
                elif v3 == 4:
                    v7 = v4[0]
                    v1 = max(v1, v7[0])
            return v1
        v1 = [[] for v2 in range(len(a2))]
        for v3, v4 in a1:
            v1[v3].append(v4)
            v1[v4].append(v3)
        return iter_dfs()
