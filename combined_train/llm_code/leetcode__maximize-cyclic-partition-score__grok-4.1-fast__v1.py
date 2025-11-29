class C1:

    def maximumScore(self, a1, a2):
        v1 = len(a1)
        v2 = 0
        for v3 in range(1, v1):
            if a1[v3] < a1[v2]:
                v2 = v3

        def compute(a1):
            v1 = a1[a1:] + a1[:a1]
            v2 = [0] * (v1 + 1)
            v3 = 0
            for v4 in range(a2):
                v5 = [float('-inf')] * (v1 + 1)
                v5[0] = 0
                v6 = float('-inf')
                v7 = float('-inf')
                for v8 in range(v1):
                    v9 = v1[v8]
                    v6 = max(v6, v2[v8] - v9)
                    v7 = max(v7, v2[v8] + v9)
                    v5[v8 + 1] = max(v5[v8], v6 + v9, v7 - v9)
                v2 = v5
                v3 = max(v3, v2[v1])
            return v3
        return max(compute(v2), compute((v2 + 1) % v1))
