import collections

class C1(object):

    def maxProfit(self, a1, a2, a3, a4, a5):
        """
        """

        def iter_dfs():
            v1 = []
            v2 = [(1, (0, v1))]
            while v2:
                v3, v4 = v2.pop()
                if v3 == 1:
                    v5, v1 = v4
                    v1[:] = [collections.defaultdict(int) for v6 in range(2)]
                    v1[0][0] = v1[1][0] = 0
                    v2.append((4, (v5, v1)))
                    v2.append((2, (v5, 0, v1)))
                elif v3 == 2:
                    v5, v7, v1 = v4
                    if v7 == len(adj[v5]):
                        continue
                    v8 = adj[v5][v7]
                    v2.append((2, (v5, v7 + 1, v1)))
                    v9 = []
                    v2.append((3, (v9, v1)))
                    v2.append((1, (v8, v9)))
                elif v3 == 3:
                    v9, v1 = v4
                    for v7 in range(2):
                        for v10, v11 in list(v1[v7].items()):
                            for v12, v13 in v9[v7].items():
                                if v10 + v12 <= a5:
                                    v1[v7][v10 + v12] = max(v1[v7][v10 + v12], v11 + v13)
                elif v3 == 4:
                    v5, v1 = v4
                    v9 = [collections.defaultdict(int) for v6 in range(2)]
                    for v7 in range(2):
                        for v14, v8 in v1[0].items():
                            v9[v7][v14] = max(v9[v7][v14], v8)
                        v15 = a2[v5] >> v7
                        if v15 > a5:
                            continue
                        v16 = a3[v5] - v15
                        for v14, v8 in v1[1].items():
                            if v14 + v15 <= a5:
                                v9[v7][v14 + v15] = max(v9[v7][v14 + v15], v8 + v16)
                    v1[:] = v9
            return max(v1[0].values())
        v1 = [[] for v2 in range(a1)]
        for v3, v4 in a4:
            v1[v3 - 1].append(v4 - 1)
        return iter_dfs()
