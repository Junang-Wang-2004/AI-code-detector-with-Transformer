class C1(object):

    def maxTargetNodes(self, a1, a2, a3):
        """
        """

        def tree_dp(a1, a2):

            def dfs1(a1, a2):
                for v1 in a1[a1]:
                    if v1 == a2:
                        continue
                    dfs1(v1, a1)
                dp[a1][0] += 1
                for v1 in a1[a1]:
                    if v1 == a2:
                        continue
                    for v2 in range(a2):
                        dp[a1][v2 + 1] += dp[v1][v2]

            def dfs2(a1, a2, a3):

                def update(a1, a2, a3):
                    v1 = [0] * len(a3)
                    for v2 in range(len(a3) - 1):
                        v1[v2 + 1] = a3[v2] + (dp[a2][v2] - (dp[a1][v2 - 1] if v2 - 1 >= 0 else 0))
                    return v1
                for v1 in a1[a1]:
                    if v1 == a2:
                        continue
                    dfs2(v1, a1, update(v1, a1, a3))
                result[a1] = sum((dp[a1][i] + a3[i] for v2 in range(len(a3))))
            v1 = [0] * len(a1)
            a2 = min(a2, len(a1) - 1)
            if a2 == -1:
                return v1
            v3 = [[0] * (a2 + 1) for v4 in range(len(a1))]
            dfs1(0, -1)
            dfs2(0, -1, [0] * (a2 + 1))
            return v1

        def find_adj(a1):
            v1 = [[] for v2 in range(len(a1) + 1)]
            for v3, v4 in a1:
                v1[v3].append(v4)
                v1[v4].append(v3)
            return v1
        v1 = find_adj(a2)
        v2 = max(tree_dp(v1, a3 - 1))
        v3 = find_adj(a1)
        return [v2 + x for v4 in tree_dp(v3, a3)]
