class C1(object):

    def placedCoins(self, a1, a2):
        """
        """

        def iter_dfs():
            v1 = [0] * len(a2)
            v2 = [(1, (0, -1, [a2[0]]))]
            while v2:
                v3, v4 = v2.pop()
                if v3 == 1:
                    v5, v6, v7 = v4
                    v2.append((4, (v5, v7)))
                    v2.append((2, (v5, v6, 0, v7)))
                elif v3 == 2:
                    v5, v6, v8, v7 = v4
                    if v8 == len(adj[v5]):
                        continue
                    v9 = adj[v5][v8]
                    v2.append((2, (v5, v6, v8 + 1, v7)))
                    if v9 == v6:
                        continue
                    v10 = [a2[v9]]
                    v2.append((3, (v10, v7)))
                    v2.append((1, (v9, v5, v10)))
                elif v3 == 3:
                    v10, v7 = v4
                    v7.extend(v10)
                    v7.sort()
                    if len(v7) > 5:
                        v7 = v7[:2] + v7[-3:]
                elif v3 == 4:
                    v5, v7 = v4
                    v1[v5] = 1 if len(v7) < 3 else max(v7[0] * v7[1] * v7[-1], v7[-3] * v7[-2] * v7[-1], 0)
            return v1
        v1 = [[] for v2 in range(len(a2))]
        for v3, v4 in a1:
            v1[v3].append(v4)
            v1[v4].append(v3)
        return iter_dfs()
