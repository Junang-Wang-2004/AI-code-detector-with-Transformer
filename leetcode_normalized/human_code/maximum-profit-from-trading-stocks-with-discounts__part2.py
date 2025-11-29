import collections

class C1(object):

    def maxProfit(self, a1, a2, a3, a4, a5):
        """
        """

        def dfs(a1):
            v1 = [collections.defaultdict(int) for v2 in range(2)]
            v1[0][0] = v1[1][0] = 0
            for v3 in adj[a1]:
                v4 = dfs(v3)
                for v5 in range(2):
                    for v6, v7 in list(v1[v5].items()):
                        for v8, v9 in v4[v5].items():
                            if v6 + v8 <= a5:
                                v1[v5][v6 + v8] = max(v1[v5][v6 + v8], v7 + v9)
            v10 = [collections.defaultdict(int) for v2 in range(2)]
            for v5 in range(2):
                for v11, v3 in v1[0].items():
                    v10[v5][v11] = max(v10[v5][v11], v3)
                v12 = a2[a1] >> v5
                if v12 > a5:
                    continue
                v13 = a3[a1] - v12
                for v11, v3 in v1[1].items():
                    if v11 + v12 <= a5:
                        v10[v5][v11 + v12] = max(v10[v5][v11 + v12], v3 + v13)
            return v10
        v1 = [[] for v2 in range(a1)]
        for v3, v4 in a4:
            v1[v3 - 1].append(v4 - 1)
        return max(dfs(0)[0].values())
