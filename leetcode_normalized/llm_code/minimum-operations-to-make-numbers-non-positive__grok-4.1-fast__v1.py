class C1:

    def minOperations(self, a1, a2, a3):
        if not a1:
            return 0
        v1 = 0
        for v2 in a1:
            v1 = max(v1, (v2 + a3 - 1) // a3)

        def compute_cost(a1):
            v1 = 0
            for v2 in a1:
                v3 = v2 - a1 * a3
                if v3 > 0:
                    v1 += (v3 + a2 - 1) // a2
            return a1 + v1
        v3 = 0
        v4 = v1
        while v4 - v3 >= 3:
            v5 = v3 + (v4 - v3) // 3
            v6 = v4 - (v4 - v3) // 3
            v7 = compute_cost(v5)
            v8 = compute_cost(v6)
            if v7 <= v8:
                v4 = v6
            else:
                v3 = v5
        v9 = float('inf')
        for v10 in range(v3, v4 + 1):
            v9 = min(v9, compute_cost(v10))
        return v9
