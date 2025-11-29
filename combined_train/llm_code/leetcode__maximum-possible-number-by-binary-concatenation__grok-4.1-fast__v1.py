class C1:

    def maxGoodNumber(self, a1):
        v1 = [format(x, 'b') for v2 in a1]
        v3 = len(v1)
        v4 = [False] * v3
        v5 = 0

        def dfs(a1):
            nonlocal max_value
            if len(a1) == v3:
                v1 = int(''.join(a1), 2)
                if v1 > v5:
                    v2 = v1
                return
            for v3 in range(v3):
                if not v4[v3]:
                    v4[v3] = True
                    dfs(a1 + [v1[v3]])
                    v4[v3] = False
        dfs([])
        return v5
