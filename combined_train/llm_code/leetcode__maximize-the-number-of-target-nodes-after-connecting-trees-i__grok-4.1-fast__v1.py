class C1:

    def maxTargetNodes(self, a1, a2, a3):

        def build_adj(a1):
            v1 = len(a1) + 1
            v2 = [[] for v3 in range(v1)]
            for v4, v5 in a1:
                v2[v4].append(v5)
                v2[v5].append(v4)
            return v2

        def ball_counts(a1, a2):
            v1 = len(a1)
            if a2 < 0:
                return [0] * v1
            v2 = min(a2, v1 - 1)
            v3 = [[0] * (v2 + 1) for v4 in range(v1)]

            def dfs_down(a1, a2):
                v3[a1][0] = 1
                for v1 in a1[a1]:
                    if v1 != a2:
                        dfs_down(v1, a1)
                        for v2 in range(v2):
                            v3[a1][v2 + 1] += v3[v1][v2]
            dfs_down(0, -1)
            v5 = [0] * v1

            def dfs_up(a1, a2, a3):
                v1 = sum((v3[a1][d] + a3[d] for v2 in range(v2 + 1)))
                v5[a1] = v1
                for v3 in a1[a1]:
                    if v3 == a2:
                        continue
                    v4 = [0] * (v2 + 1)
                    for v2 in range(v2):
                        v5 = v3[v3][v2 - 1] if v2 > 0 else 0
                        v6 = v3[a1][v2] - v5
                        v4[v2 + 1] = a3[v2] + v6
                    dfs_up(v3, a1, v4)
            v6 = [0] * (v2 + 1)
            dfs_up(0, -1, v6)
            return v5
        v1 = build_adj(a2)
        v2 = ball_counts(v1, a3 - 1)
        v3 = max(v2)
        v4 = build_adj(a1)
        v5 = ball_counts(v4, a3)
        return [v5[i] + v3 for v6 in range(len(v5))]
