class C1(object):

    def minimumFuelCost(self, a1, a2):
        """
        """

        def ceil_divide(a1, a2):
            return (a1 + a2 - 1) // a2

        def iter_dfs():
            v1 = 0
            v2 = [(1, (0, -1, 0, [1]))]
            while v2:
                v3, v4 = v2.pop()
                if v3 == 1:
                    v5, v6, v7, v8 = v4
                    v2.append((3, (v7, v8)))
                    for v9 in adj[v5]:
                        if v9 == v6:
                            continue
                        v10 = [1]
                        v2.append((2, (v10, v8)))
                        v2.append((1, (v9, v5, v7 + 1, v10)))
                elif v3 == 2:
                    v10, v8 = v4
                    v8[0] += v10[0]
                elif v3 == 3:
                    v7, v8 = v4
                    if v7:
                        v1 += ceil_divide(v8[0], a2)
            return v1
        v1 = [[] for v2 in range(len(a1) + 1)]
        for v3, v4 in a1:
            v1[v3].append(v4)
            v1[v4].append(v3)
        return iter_dfs()
