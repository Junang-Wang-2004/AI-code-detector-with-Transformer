class C1:

    def minCostToEqualizeArray(self, a1, a2, a3):
        v1 = 10 ** 9 + 7
        v2 = len(a1)
        v3 = max(a1)
        v4 = sum(a1)
        v5 = v3 * v2 - v4
        if v2 <= 2 or a2 * 2 <= a3:
            return v5 * a2 % v1
        v6 = min(a1)
        v7 = v3 - v6
        v8 = max(0, 2 * v7 - v5)

        def get_cost(a1, a2):
            v1 = a1 - a2
            v2 = a2 + v1 % 2
            v3 = v1 // 2
            return v2 * a2 + v3 * a3
        v9 = get_cost(v5, v8)
        v10 = v2 - 2
        v11, v12 = divmod(v8, v10)
        v13 = v5 + v2 * v11
        v9 = min(v9, get_cost(v13, v12))
        v13 += v2
        v9 = min(v9, v13 % 2 * a2 + v13 // 2 * a3)
        v13 += v2
        v9 = min(v9, v13 % 2 * a2 + v13 // 2 * a3)
        return v9 % v1
