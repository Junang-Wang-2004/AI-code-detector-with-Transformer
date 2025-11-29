class C1:

    def placedCoins(self, a1, a2):
        v1 = len(a2)
        v2 = [[] for v3 in range(v1)]
        for v4, v5 in a1:
            v2[v4].append(v5)
            v2[v5].append(v4)
        v6 = [0] * v1

        def dfs(a1, a2):
            v1 = a2[a1]
            v2 = [v1]
            v3 = [v1]
            v4 = 1
            for v5 in v2[a1]:
                if v5 == a2:
                    continue
                v6, v7, v8 = dfs(v5, a1)
                v4 += v8
                v9 = sorted(v2 + v6)[:2]
                v2 = v9
                v10 = sorted(v3 + v7, reverse=True)[:3]
                v3 = v10
            if v4 < 3:
                v6[a1] = 1
            else:
                v11 = v2[0] * v2[1] * v3[0]
                v12 = v3[0] * v3[1] * v3[2]
                v6[a1] = max(v11, v12, 0)
            return (v2, v3, v4)
        dfs(0, -1)
        return v6
