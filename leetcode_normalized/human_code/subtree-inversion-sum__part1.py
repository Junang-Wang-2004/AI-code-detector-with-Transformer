class C1(object):

    def subtreeInversionSum(self, a1, a2, a3):
        """
        """

        def iter_dfs():
            v1 = []
            v2 = [0] * 3
            v3 = [(1, (0, -1, v2))]
            while v3:
                v4, v5 = v3.pop()
                if v4 == 1:
                    v6, v7, v2 = v5
                    v1.append([0] * 2)
                    v2[:] = [a2[v6], 0, 0]
                    v3.append((4, (v6, v7, v2)))
                    v3.append((2, (v6, v7, v2, 0)))
                elif v4 == 2:
                    v6, v7, v2, v8 = v5
                    if v8 == len(adj[v6]):
                        continue
                    v9 = adj[v6][v8]
                    v3.append((2, (v6, v7, v2, v8 + 1)))
                    if v9 == v7:
                        continue
                    v10 = [0] * 3
                    v3.append((3, (v6, v7, v10, v2, v8)))
                    v3.append((1, (v9, v6, v10)))
                elif v4 == 3:
                    v6, v7, v10, v2, v8 = v5
                    v2[0] += v10[0]
                    v2[1] += v10[1]
                    v2[2] += v10[2]
                elif v4 == 4:
                    v6, v7, v2 = v5
                    v2[1] = max(v2[1], v1[-1][1] - 2 * v2[0])
                    v2[2] = max(v2[2], v1[-1][0] + 2 * v2[0])
                    v1.pop()
                    if len(v1) - a3 >= 0:
                        v1[len(v1) - a3][0] += v2[1]
                        v1[len(v1) - a3][1] += v2[2]
            return v2[0] + v2[1]
        v1 = [[] for v2 in range(len(a2))]
        for v3, v4 in a1:
            v1[v3].append(v4)
            v1[v4].append(v3)
        return iter_dfs()
