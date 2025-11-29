class C1:

    def getLengthOfOptimalCompression(self, a1, a2):
        v1 = len(a1)
        v2 = v1 + 1
        v3 = [[-1] * (a2 + 1) for v4 in range(v1 + 1)]

        def group_cost(a1):
            if a1 < 2:
                return a1
            return 1 + len(str(a1))

        def solve(a1, a2):
            if a1 == v1:
                return 0
            if v3[a1][a2] != -1:
                return v3[a1][a2]
            v1 = v2
            if a2 > 0:
                v1 = solve(a1 + 1, a2 - 1)
            v2 = a1[a1]
            v3 = 0
            v4 = 0
            for v5 in range(a1, v1):
                if a1[v5] == v2:
                    v3 += 1
                else:
                    v4 += 1
                if v4 > a2:
                    break
                v1 = min(v1, group_cost(v3) + solve(v5 + 1, a2 - v4))
            v3[a1][a2] = v1
            return v1
        return solve(0, a2)
