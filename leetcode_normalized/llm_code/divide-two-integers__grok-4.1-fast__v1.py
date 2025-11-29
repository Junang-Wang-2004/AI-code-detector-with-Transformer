class C1:

    def divide(self, a1, a2):
        v1 = 1 if (a1 > 0) == (a2 > 0) else -1
        v2, v3 = (abs(a1), abs(a2))
        v4 = 0
        for v5 in range(31, -1, -1):
            if v2 >= v3 << v5:
                v2 -= v3 << v5
                v4 |= 1 << v5
        v6 = v1 * v4
        v7 = -(1 << 31)
        v8 = (1 << 31) - 1
        return max(v7, min(v6, v8))
