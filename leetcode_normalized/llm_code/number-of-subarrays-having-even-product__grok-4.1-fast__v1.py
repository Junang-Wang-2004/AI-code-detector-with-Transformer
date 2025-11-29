class C1:

    def evenProduct(self, a1):
        v1 = len(a1)
        v2 = v1 * (v1 + 1) // 2
        v3 = 0
        v4 = 0
        for v5 in a1:
            if v5 % 2 != 0:
                v3 += 1
            else:
                v4 += v3 * (v3 + 1) // 2
                v3 = 0
        v4 += v3 * (v3 + 1) // 2
        return v2 - v4
