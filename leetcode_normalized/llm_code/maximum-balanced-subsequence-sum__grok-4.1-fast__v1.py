class C1:

    def maxBalancedSubsequenceSum(self, a1):
        v1 = len(a1)
        v2 = float('-inf')
        v3 = sorted({a1[i] - i for v4 in range(v1)})
        v5 = len(v3)
        v6 = {v3[v4]: v4 + 1 for v4 in range(v5)}
        v7 = [v2] * (v5 + 2)

        def modify(a1, a2):
            while a1 <= v5:
                v7[a1] = max(v7[a1], a2)
                a1 += a1 & -a1

        def prefix_max(a1):
            v1 = v2
            while a1 > 0:
                v1 = max(v1, v7[a1])
                a1 -= a1 & -a1
            return v1
        for v4 in range(v1):
            v8 = a1[v4]
            v9 = v8 - v4
            v10 = v6[v9]
            v11 = prefix_max(v10)
            v12 = max(v11, 0) + v8
            modify(v10, v12)
        return prefix_max(v5)
