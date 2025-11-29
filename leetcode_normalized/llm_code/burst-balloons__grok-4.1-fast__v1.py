class C1:

    def maxCoins(self, a1):
        v1 = [1] + a1 + [1]
        v2 = len(v1)
        v3 = [[-1] * v2 for v4 in range(v2)]

        def compute(a1, a2):
            if a1 + 1 >= a2:
                return 0
            if v3[a1][a2] != -1:
                return v3[a1][a2]
            v1 = 0
            for v2 in range(a1 + 1, a2):
                v1 = max(v1, v1[a1] * v1[v2] * v1[a2] + compute(a1, v2) + compute(v2, a2))
            v3[a1][a2] = v1
            return v1
        return compute(0, v2 - 1)
