class C1(object):

    def countGoodNodes(self, a1):
        """
        """

        def iter_dfs():
            v1 = 0
            v2 = [(1, (0, -1, [0]))]
            while v2:
                v3, v4 = v2.pop()
                if v3 == 1:
                    v5, v6, v7 = v4
                    v8, v9 = ([0], [True])
                    v2.append((4, (v7, v9)))
                    v2.append((2, (v5, v6, 0, v7, v8, v9)))
                elif v3 == 2:
                    v5, v6, v10, v7, v8, v9 = v4
                    if v10 == len(adj[v5]):
                        continue
                    v2.append((2, (v5, v6, v10 + 1, v7, v8, v9)))
                    v11 = adj[v5][v10]
                    if v11 == v6:
                        continue
                    v12 = [0]
                    v2.append((3, (v12, v7, v8, v9)))
                    v2.append((1, (v11, v5, v12)))
                elif v3 == 3:
                    v12, v7, v8, v9 = v4
                    v7[0] += v12[0]
                    v8[0] += 1
                    if v12[0] * v8[0] != v7[0]:
                        v9[0] = False
                elif v3 == 4:
                    v7, v9 = v4
                    if v9[0]:
                        v1 += 1
                    v7[0] += 1
            return v1
        v1 = [[] for v2 in range(len(a1) + 1)]
        for v3, v4 in a1:
            v1[v3].append(v4)
            v1[v4].append(v3)
        return iter_dfs()
