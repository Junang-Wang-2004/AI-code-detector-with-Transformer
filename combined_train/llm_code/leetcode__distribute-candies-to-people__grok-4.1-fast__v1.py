class C1:

    def distributeCandies(self, a1, a2):
        v1, v2 = (0, 200000)
        while v1 < v2:
            v3 = v1 + (v2 - v1 + 1) // 2
            if v3 * (v3 + 1) // 2 <= a1:
                v1 = v3
            else:
                v2 = v3 - 1
        v4 = v1
        v5 = a1 - v4 * (v4 + 1) // 2
        v6 = [0] * a2
        v7 = v4 // a2
        v8 = v4 % a2
        for v9 in range(a2):
            v10 = v7 + (1 if v9 < v8 else 0)
            v6[v9] = v10 * (v9 + 1) + a2 * (v10 * (v10 - 1) // 2)
        if v5 > 0:
            v11 = v4 % a2
            v6[v11] += v5
        return v6
