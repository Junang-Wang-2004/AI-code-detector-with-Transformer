class C1:

    def minimumXORSum(self, a1, a2):
        v1 = len(a1)
        v2 = {}

        def dfs(a1, a2):
            if a1 == v1:
                return 0
            v1 = (a1, a2)
            if v1 in v2:
                return v2[v1]
            v2 = float('inf')
            for v3 in range(v1):
                if a2 & 1 << v3 == 0:
                    v2 = min(v2, a1[a1] ^ a2[v3] + dfs(a1 + 1, a2 | 1 << v3))
            v2[v1] = v2
            return v2
        return dfs(0, 0)
