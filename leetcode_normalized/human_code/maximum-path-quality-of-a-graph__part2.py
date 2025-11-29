class C1(object):

    def maximalPathQuality(self, a1, a2, a3):
        """
        """

        def iter_dfs(a1, a2, a3):
            v1, v2 = ([0] * len(a2), set())
            v3 = 0
            v4 = [(1, (0, a3, 0))]
            while v4:
                v5, v6 = v4.pop()
                if v5 == 1:
                    v7, v8, v9 = v6
                    v1[v7] += 1
                    if v1[v7] == 1:
                        v9 += a1[v7]
                    if not v7:
                        v3 = max(v3, v9)
                    v4.append((4, (v7,)))
                    for v10, v11 in reversed(a2[v7]):
                        if (v7, v10) in v2 or v8 < v11:
                            continue
                        v4.append((3, (v7, v10)))
                        v4.append((1, (v10, v8 - v11, v9)))
                        v4.append((2, (v7, v10)))
                elif v5 == 2:
                    v7, v10 = v6
                    v2.add((v7, v10))
                elif v5 == 3:
                    v7, v10 = v6
                    v2.remove((v7, v10))
                elif v5 == 4:
                    v7 = v6[0]
                    v1[v7] -= 1
            return v3
        v1 = [[] for v2 in range(len(a1))]
        for v3, v4, v5 in a2:
            v1[v3].append((v4, v5))
            v1[v4].append((v3, v5))
        return iter_dfs(a1, v1, a3)
