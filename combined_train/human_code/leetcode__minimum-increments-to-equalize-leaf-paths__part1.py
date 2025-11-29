class C1(object):

    def minIncrease(self, a1, a2, a3):
        """
        """

        def iter_dfs():
            v1 = a1 - 1
            v2 = [0] * len(adj)
            v3 = [(1, (0, -1))]
            while v3:
                v4, (v5, v6) = v3.pop()
                if v4 == 1:
                    v3.append((2, (v5, v6)))
                    for v7 in reversed(adj[v5]):
                        if v7 != v6:
                            v3.append((1, (v7, v5)))
                elif v4 == 2:
                    v8 = 0
                    for v7 in adj[v5]:
                        if v7 == v6 or v2[v7] < v2[v5]:
                            continue
                        if v2[v7] > v2[v5]:
                            v2[v5] = v2[v7]
                            v8 = 0
                        v8 += 1
                    v1 -= v8
                    v2[v5] += a3[v5]
            return v1
        v1 = [[] for v2 in range(a1)]
        for v3, v4 in a2:
            v1[v3].append(v4)
            v1[v4].append(v3)
        return iter_dfs()
