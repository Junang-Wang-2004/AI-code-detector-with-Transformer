class C1:

    def maxProfit(self, a1, a2):
        v1 = 10 ** 9 + 7

        def feasible(a1):
            v1 = 0
            for v2 in a1:
                if v2 >= a1:
                    v1 += v2 - a1 + 1
            return v1 <= a2
        v2 = max(a1) if a1 else 0
        v3, v4 = (1, v2 + 1)
        while v3 < v4:
            v5 = (v3 + v4) // 2
            if feasible(v5):
                v4 = v5
            else:
                v3 = v5 + 1
        v6 = v3
        v7 = 0
        v8 = 0
        for v9 in a1:
            if v9 >= v6:
                v10 = v9 - v6 + 1
                v8 += v10
                v7 += v10 * v6 + v10 * (v10 - 1) // 2
        v11 = a2 - v8
        return (v7 + v11 * (v6 - 1)) % v1
