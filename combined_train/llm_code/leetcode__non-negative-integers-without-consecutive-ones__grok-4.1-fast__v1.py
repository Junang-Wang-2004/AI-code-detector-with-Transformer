class C1:

    def findIntegers(self, a1):
        v1 = [a1 >> i & 1 for v2 in range(30, -1, -1)]
        v3 = {}

        def dfs(a1, a2, a3):
            if a1 == 31:
                return 1
            v1 = (a1, a2, a3)
            if v1 in v3:
                return v3[v1]
            v2 = 0
            v3 = v1[a1] if a2 else 1
            for v4 in range(v3 + 1):
                if v4 == 1 and a3:
                    continue
                v5 = 1 if a2 and v4 == v3 else 0
                v2 += dfs(a1 + 1, v5, v4)
            v3[v1] = v2
            return v2
        return dfs(0, 1, 0)
