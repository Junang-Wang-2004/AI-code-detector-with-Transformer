class C1(object):

    def minimumDiameterAfterMerge(self, a1, a2):
        """
        """

        def ceil_divide(a1, a2):
            return (a1 + a2 - 1) // 2

        def tree_diameter(a1):

            def bfs():
                v1 = 0
                v2 = [0] * len(adj)
                v3 = list(map(len, adj))
                v4 = [u for v5 in range(len(v3)) if v3[v5] == 1]
                while v4:
                    v6 = []
                    for v5 in v4:
                        if v3[v5] == 0:
                            continue
                        v3[v5] -= 1
                        for v7 in adj[v5]:
                            if v3[v7] == 0:
                                continue
                            v1 = max(v1, v2[v7] + (v2[v5] + 1))
                            v2[v7] = max(v2[v7], v2[v5] + 1)
                            v3[v7] -= 1
                            if v3[v7] == 1:
                                v6.append(v7)
                    v4 = v6
                return v1
            v1 = [[] for v2 in range(len(a1) + 1)]
            for v3, v4 in a1:
                v1[v3].append(v4)
                v1[v4].append(v3)
            return bfs()
        v1 = tree_diameter(a1)
        v2 = tree_diameter(a2)
        return max(ceil_divide(v1, 2) + 1 + ceil_divide(v2, 2), v1, v2)
