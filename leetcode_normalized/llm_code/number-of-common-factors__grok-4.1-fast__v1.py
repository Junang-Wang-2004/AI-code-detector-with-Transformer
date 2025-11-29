class C1:

    def commonFactors(self, a1, a2):
        v1, v2 = (a1, a2)
        while v2:
            v1, v2 = (v2, v1 % v2)
        v3 = v1
        v4 = 0
        for v5 in range(1, int(v3 ** 0.5) + 1):
            if v3 % v5 == 0:
                v4 += 1 if v5 * v5 == v3 else 2
        return v4
