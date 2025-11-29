class C1:

    def maximumPoints(self, a1, a2, a3):
        v1 = len(a2)
        v2 = [[] for v3 in range(v1)]
        for v4, v5 in a1:
            v2[v4].append(v5)
            v2[v5].append(v4)
        v6 = max(a2)
        v7 = v6.bit_length() + 1

        def dfs(a1, a2):
            v1 = [dfs(v, a1) for v2 in v2[a1] if v2 != a2]
            v3 = [0] * (v7 + 1)
            for v4 in range(v7 + 1):
                v5 = (a2[a1] >> v4) - a3
                for v6 in v1:
                    v5 += v6[v4]
                v7 = a2[a1] >> v4 + 1
                for v6 in v1:
                    v7 += v6[v4 + 1] if v4 + 1 <= v7 else 0
                v3[v4] = max(v5, v7)
            return v3
        return dfs(0, -1)[0]
