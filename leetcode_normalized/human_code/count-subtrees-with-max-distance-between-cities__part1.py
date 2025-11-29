import collections

class C1(object):

    def countSubgraphsForEachDiameter(self, a1, a2):
        """
        """

        def dfs(a1, a2, a3, a4, a5, a6, a7):
            for v1 in a2[a3]:
                if v1 == a4 or a5[v1]:
                    continue
                dfs(a1, a2, v1, a3, a5, a6, a7)
            a7[a3][0][0] = 1
            for v1 in a2[a3]:
                if v1 == a4 or a5[v1]:
                    continue
                v2 = [row[:] for v3 in a7[a3]]
                for v4 in range(a6[a3]):
                    for v5 in range(v4, min(2 * v4 + 1, a6[a3])):
                        if not a7[a3][v4][v5]:
                            continue
                        for v6 in range(a6[v1]):
                            for v7 in range(v6, min(2 * v6 + 1, a6[v1])):
                                v2[max(v4, v6 + 1)][max(v5, v7, v4 + v6 + 1)] += a7[a3][v4][v5] * a7[v1][v6][v7]
                a6[a3] += a6[v1]
                a7[a3] = v2
        v1 = collections.defaultdict(list)
        for v2, v3 in a2:
            v2 -= 1
            v3 -= 1
            v1[v2].append(v3)
            v1[v3].append(v2)
        v4, v5 = ([0] * a1, [0] * (a1 - 1))
        for v6 in range(a1):
            v7 = [[[0] * a1 for v8 in range(a1)] for v8 in range(a1)]
            v9 = [1] * a1
            dfs(a1, v1, v6, -1, v4, v9, v7)
            v4[v6] = 1
            for v10 in range(1, a1):
                for v11 in range(v10, min(2 * v10 + 1, a1)):
                    v5[v11 - 1] += v7[v6][v10][v11]
        return v5
